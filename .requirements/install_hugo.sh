#!/usr/bin/env bash
set -euo pipefail

# install-hugo-portable.sh
# Installs a working Hugo Extended on Debian by:
# 1) Trying latest tar.gz binaries
# 2) Falling back to Linux-64bit variant
# 3) Backtracking through older releases
# 4) Finally building from source if needed
#
# Env knobs:
#   HUGO_VERSION=0.150.0     Pin to a version tag (with or without leading v)
#   MAX_BACKTRACK=20         How many older releases to try
#   INSTALL_PREFIX=/usr/local  Prefix for final binary install
#   NO_APT=1                 Skip apt install of deps
#   FORCE_BUILD=1            Skip binaries and build from source directly

INSTALL_PREFIX="${INSTALL_PREFIX:-/usr/local}"
MAX_BACKTRACK="${MAX_BACKTRACK:-20}"

need() { command -v "$1" >/dev/null 2>&1; }
die() { echo "[ERROR] $*" >&2; exit 1; }
log() { echo "[INFO] $*"; }

if [[ "${NO_APT:-}" != "1" ]]; then
  sudo apt-get update -y
  sudo apt-get install -y curl jq ca-certificates tar coreutils git gcc
fi

need curl || die "curl required"
need jq || die "jq required"
need tar || die "tar required"

arch="$(uname -m)"
case "$arch" in
  x86_64|amd64) gh_arch="amd64"; netlify_arch="Linux-64bit";;
  aarch64|arm64) gh_arch="arm64"; netlify_arch="Linux-ARM64";;
  *) die "Unsupported arch: ${arch}. Supported: x86_64, aarch64";;
esac

api_list_latest="https://api.github.com/repos/gohugoio/hugo/releases"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

get_releases() {
  # Returns a JSON array of non prerelease, non draft releases newest first
  curl -fsSL "${api_list_latest}?per_page=100" \
  | jq '[ .[] | select(.prerelease|not) | select(.draft|not) ]'
}

pick_assets_for_tag() {
  # Args: tag version without v and with v in variables ver and tag
  local ver="$1" tag="v$1"
  # Candidate asset names to try, in order
  local cands=()
  # Standard linux tarball
  cands+=("hugo_extended_${ver}_linux-${gh_arch}.tar.gz")
  # Netlify archive variant where it exists
  if [[ "$gh_arch" == "amd64" ]]; then
    cands+=("hugo_extended_${ver}_${netlify_arch}.tar.gz")
  fi
  printf '%s\n' "${cands[@]}"
}

download_and_try() {
  # Args: tag name with v, ver without v
  local tag="$1" ver="$2"
  local checks="hugo_${ver}_checksums.txt"

  # Build list of candidate assets for this tag
  mapfile -t assets < <(pick_assets_for_tag "$ver")

  for name in "${assets[@]}"; do
    local tar_url="https://github.com/gohugoio/hugo/releases/download/${tag}/${name}"
    local chk_url="https://github.com/gohugoio/hugo/releases/download/${tag}/${checks}"

    log "Trying asset ${name} for ${tag}"
    rm -f "$tmp/$name" "$tmp/checksums.txt" "$tmp/hugo" || true
    if ! curl -fL "$tar_url" -o "$tmp/$name"; then
      log "Asset not found: $name"
      continue
    fi
    if ! curl -fL "$chk_url" -o "$tmp/checksums.txt"; then
      log "Checksums file missing for ${tag}"
      continue
    fi

    # Verify checksum
    local match
    match="$(grep -E "[[:xdigit:]]{64}[[:space:]]+${name}$" "$tmp/checksums.txt" || true)"
    if [[ -z "$match" ]]; then
      log "Checksum entry not found for ${name}. Skipping."
      continue
    fi
    if ! printf '%s\n' "$match" | sha256sum -c -; then
      log "Checksum failed for ${name}. Skipping."
      continue
    fi

    # Extract and smoke test
    tar -xzf "$tmp/$name" -C "$tmp" hugo
    if "$tmp/hugo" version >/dev/null 2>&1; then
      log "Binary runs on this system. Installing to ${INSTALL_PREFIX}/bin/hugo"
      sudo install -m 0755 -D "$tmp/hugo" "${INSTALL_PREFIX}/bin/hugo"
      return 0
    else
      log "Binary does not run on this system. Will try other assets or older releases."
    fi
  done

  return 1
}

build_from_source() {
  log "Falling back to building Hugo Extended from source"
  # Install or update Go if missing or too old
  if ! need go; then
    GO_VERSION="${GO_VERSION:-1.24.0}"
    tarball="go${GO_VERSION}.linux-${gh_arch}.tar.gz"
    url="https://go.dev/dl/${tarball}"
    log "Installing Go ${GO_VERSION} to /usr/local"
    curl -fL "$url" -o "$tmp/$tarball"
    sudo rm -rf /usr/local/go
    sudo tar -C /usr/local -xzf "$tmp/$tarball"
    export PATH="/usr/local/go/bin:${PATH}"
  fi

  # Ensure GOBIN is set for predictable location
  export GOBIN="${tmp}/gobin"
  mkdir -p "$GOBIN"

  log "Compiling with: CGO_ENABLED=1 go install -tags extended github.com/gohugoio/hugo@latest"
  CGO_ENABLED=1 go install -tags extended github.com/gohugoio/hugo@latest

  [[ -x "${GOBIN}/hugo" ]] || die "Build did not produce ${GOBIN}/hugo"
  if ! "${GOBIN}/hugo" version >/dev/null 2>&1; then
    die "Built binary does not run"
  fi
  sudo install -m 0755 -D "${GOBIN}/hugo" "${INSTALL_PREFIX}/bin/hugo"
}

main() {
  if [[ "${FORCE_BUILD:-}" == "1" ]]; then
    build_from_source
    "${INSTALL_PREFIX}/bin/hugo" version
    return 0
  fi

  if [[ -n "${HUGO_VERSION:-}" ]]; then
    ver="${HUGO_VERSION#v}"
    tag="v${ver}"
    if download_and_try "$tag" "$ver"; then
      "${INSTALL_PREFIX}/bin/hugo" version
      return 0
    else
      log "Pinned version ${tag} failed. Falling back to source build."
      build_from_source
      "${INSTALL_PREFIX}/bin/hugo" version
      return 0
    fi
  fi

  log "Resolving newest compatible Hugo Extended..."
  releases_json="$(get_releases)" || die "Failed to list releases"

  # Try latest first
  first_tag="$(jq -r '.[0].tag_name' <<<"$releases_json")"
  first_ver="${first_tag#v}"
  if download_and_try "$first_tag" "$first_ver"; then
    "${INSTALL_PREFIX}/bin/hugo" version
    return 0
  fi

  # Walk back through older releases
  tried=1
  total="$(jq 'length' <<<"$releases_json")"
  for idx in $(seq 1 $((total-1))); do
    if (( tried >= MAX_BACKTRACK )); then break; fi
    tag="$(jq -r ".[$idx].tag_name" <<<"$releases_json")"
    ver="${tag#v}"
    if download_and_try "$tag" "$ver"; then
      "${INSTALL_PREFIX}/bin/hugo" version
      return 0
    fi
    tried=$((tried+1))
  done

  log "No prebuilt binary ran successfully within ${MAX_BACKTRACK} releases."
  build_from_source
  "${INSTALL_PREFIX}/bin/hugo" version
}

main "$@"

