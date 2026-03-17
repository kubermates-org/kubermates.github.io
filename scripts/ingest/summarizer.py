# scripts/ingest/summarizer.py
from __future__ import annotations
import os, json, time, hashlib, pathlib, textwrap, re
from typing import Dict, List, Optional

import requests
from bs4 import BeautifulSoup

# -----------------------------
# Config & cache
# -----------------------------
CACHE_PATH = pathlib.Path(".cache/summaries.json")
CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)

# Default to Haiku 4.5 for cost-effective batch summarization.
# Override with ANTHROPIC_MODEL env var (e.g. claude-sonnet-4-6 for higher quality).
DEFAULT_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-haiku-4-5")

# Map-Reduce chunk size in characters (ensure full-page coverage)
MAX_CHARS_PER_CHUNK = int(os.getenv("SUMMARY_CHUNK_CHARS", "12000"))

# Boilerplate/UX noise to drop (sentences or lines containing any of these)
_NOISE_PATTERNS = [
    r"\bcookie(s)?\b",
    r"\bsubscribe\b", r"\bnewsletter\b",
    r"\bsign in\b", r"\blog in\b",
    r"\bprivacy policy\b", r"\bterms of service\b",
    r"\bad(s|vertisement|choices)?\b",
    r"\bmanage preferences\b",
    r"\baccept all\b", r"\breject all\b",
    r"\bThere was an error while loading\. Please reload this page\.",
    r"\bEnable JavaScript\b",
    r"\bSkip to content\b",
    r"\bJoin GitHub\b",
    r"\bUse (the )?GitHub (App|Desktop)\b",
    r"\bOpen (in|this) app\b",
    r"\bBack to top\b",
]

# Common classes/ids to strip before extracting text
_STRIP_SELECTORS = [
    "script", "style", "noscript",
    "header", "nav", "footer", "aside",
    ".cookie", ".cookies", "#cookie", "#cookies",
    ".banner", ".announcement", ".promo", ".ads", ".ad", ".advert",
    ".newsletter", ".subscribe", ".subscription",
    ".modal", ".toast", ".popover", ".tooltip",
    ".breadcrumbs", ".breadcrumb",
    ".pagination", ".pager",
    ".sr-only", "[aria-live]", "[role=alert]", "[role=status]",
    "div[data-test-selector='notifications-link']",
    "div[data-test-selector='header-search']", ".flash", ".Header", ".footer",
    ".Box-header", ".js-flash-alert", ".js-notice",
]

# -----------------------------
# Utilities
# -----------------------------
def _load_cache() -> Dict[str, Dict]:
    if CACHE_PATH.exists():
        try:
            return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}

def _save_cache(cache: Dict[str, Dict]):
    CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")

def _hash_key(*parts: str) -> str:
    h = hashlib.sha256()
    for p in parts:
        h.update((p or "").encode("utf-8"))
        h.update(b"\x00")
    return h.hexdigest()

def _normalize_whitespace(s: str) -> str:
    return " ".join((s or "").split())

def _strip_artifacts(s: str) -> str:
    """Remove leftover bullet/hash markers if the model adds them."""
    lines = [ln.strip() for ln in (s or "").splitlines()]
    clean = []
    for ln in lines:
        if ln.startswith("# Chunk"):
            continue
        if ln.startswith("- "):
            ln = ln[2:].strip()
        clean.append(ln)
    return _normalize_whitespace(" ".join(clean))

def _split_into_chunks(text: str, max_chars: int) -> List[str]:
    text = (text or "").strip()
    if not text:
        return []
    if len(text) <= max_chars:
        return [text]
    paras = [p.strip() for p in text.split("\n") if p.strip()]
    chunks, cur, cur_len = [], [], 0
    for p in paras:
        if cur_len + len(p) + 1 <= max_chars:
            cur.append(p)
            cur_len += len(p) + 1
        else:
            if cur:
                chunks.append("\n".join(cur))
            cur = [p]
            cur_len = len(p)
    if cur:
        chunks.append("\n".join(cur))
    return chunks

def _anthropic_client():
    import anthropic
    return anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

# -----------------------------
# Version-string protection
# -----------------------------
_VERSION_RE = re.compile(r"\b(v?\d+(?:\.\d+){1,4})\b")

def _protect_versions(s: str) -> str:
    return _VERSION_RE.sub(lambda m: m.group(1).replace(".", "§DOT§"), s)

def _restore_versions(s: str) -> str:
    return s.replace("§DOT§", ".")

# -----------------------------
# Text noise filtering
# -----------------------------
_NOISE_RE = re.compile("|".join(_NOISE_PATTERNS), re.IGNORECASE)

def _filter_noise_text(text: str) -> str:
    """Remove cookie banners, login prompts, reload-error lines, etc."""
    if not text:
        return ""

    protected = _protect_versions(text.replace("\u00a0", " ").strip())
    parts = re.split(r"(?<=[\.\!\?])\s+", protected)

    filtered: List[str] = []
    prev = None

    for s in parts:
        s_clean = s.strip()
        if not s_clean:
            continue
        if _NOISE_RE.search(s_clean):
            continue
        if len(s_clean) < 25 and re.search(r"\b(see|read|learn)\b", s_clean, re.I):
            continue
        if prev and s_clean.lower() == prev.lower():
            continue

        filtered.append(s_clean)
        prev = s_clean

    return _restore_versions(" ".join(filtered).strip())

# -----------------------------
# HTML fetch & clean
# -----------------------------
def _pick_root(soup: BeautifulSoup, url: Optional[str]) -> BeautifulSoup:
    if url and "github.com" in url:
        gh = soup.select_one(".markdown-body")
        if gh:
            return gh
    for selector in ["article", "[role=main]", "main", "body"]:
        node = soup.select_one(selector)
        if node:
            return node
    return soup

def _strip_non_content(root: BeautifulSoup):
    for sel in _STRIP_SELECTORS:
        for tag in root.select(sel):
            tag.decompose()

def _extract_text_blocks(root: BeautifulSoup) -> str:
    blocks: List[str] = []

    for h in root.select("h1, h2, h3"):
        txt = h.get_text(" ", strip=True)
        if txt:
            blocks.append(txt)

    for p in root.find_all(["p", "li", "pre", "code"]):
        txt = p.get_text(" ", strip=True)
        if txt:
            blocks.append(txt)

    if len(blocks) < 3:
        txt = root.get_text(" ", strip=True)
        if txt:
            blocks = [txt]

    joined = "\n\n".join(blocks)
    return textwrap.dedent(joined).strip()

def _clean_html_to_text(html: str, url: Optional[str] = None) -> str:
    if not html:
        return ""
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    root = _pick_root(soup, url)
    _strip_non_content(root)
    text = _extract_text_blocks(root)

    text = _filter_noise_text(text)
    return _normalize_whitespace(text)

def fetch_full_text(url: str, timeout: int = 20) -> str:
    """Public: fetch and clean a page to plain text."""
    if not url:
        return ""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; KubermatesBot/1.0; +https://kubermates.org)"
        }
        r = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)
        if r.status_code != 200 or not r.text:
            return ""
        return _clean_html_to_text(r.text, url=url)
    except Exception:
        return ""

# -----------------------------
# JSON extraction (Claude doesn't have strict JSON mode)
# -----------------------------
def _extract_json(text: str) -> Optional[Dict]:
    """Robustly extract a JSON object from text that may contain extra content."""
    text = (text or "").strip()
    # Try direct parse first
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    # Find the outermost {...} block
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass
    return None

# -----------------------------
# Prompts (Kubernetes/cloud-native focused)
# -----------------------------
def _prompt_chunk(title: Optional[str], url: Optional[str], lang_hint: Optional[str], chunk_text: str) -> str:
    meta = []
    if title: meta.append(f'Title: "{title}"')
    if url:   meta.append(f"URL: {url}")
    if lang_hint: meta.append(f"Language hint: {lang_hint}")
    meta_str = "\n".join(meta)
    return textwrap.dedent(f"""
    You are summarizing ONE PART of a Kubernetes / cloud-native technical article. Extract the key facts from this chunk as a concise bullet list.

    Focus especially on:
    - Version numbers, API changes, deprecations, breaking changes
    - New features, flags, config options, CRDs, operators
    - Performance numbers, benchmark results
    - Security fixes, CVE references
    - Cloud provider specifics (AKS, EKS, GKE, OpenShift, Rancher…)
    - Tool/project names and their roles

    Rules:
    - Write in the SAME LANGUAGE as the source text (use the title or language hint if ambiguous).
    - Be terse and factual; no fluff, no marketing language.
    - Output PLAIN TEXT bullet points (prefix each line with "- "). No markdown fences.

    {meta_str}

    --- CHUNK START ---
    {chunk_text}
    --- CHUNK END ---
    """).strip()

def _prompt_reduce(title: Optional[str], url: Optional[str], lang_hint: Optional[str], bullets: str) -> str:
    meta = []
    if title: meta.append(f'Title: "{title}"')
    if url:   meta.append(f"URL: {url}")
    if lang_hint: meta.append(f"Language hint: {lang_hint}")
    meta_str = "\n".join(meta)
    return textwrap.dedent(f"""
    You are creating final summaries for a Kubernetes / cloud-native community site. The bullets below cover the FULL article.

    Produce a JSON object with exactly two keys:
    "tldr":    1-2 sentences (~300 chars). The single most important takeaway — what changed, what it enables, or why it matters.
    "summary": 3-6 sentences (~1000 chars). Crisp, complete overview: context, what's new, key details (versions, flags, APIs), and impact.

    Rules:
    - Use the SAME LANGUAGE as the source (use the hint/title if needed).
    - Add a relevant emoji at the start of each field to aid scannability.
    - Be faithful — only use information present in the bullets.
    - Prefer concrete details (versions, tool names, config flags) over vague descriptions.
    - Do NOT include list markers, section headers, or "# Chunk" text in either field.
    - Output ONLY the JSON object — no other text before or after it.

    {meta_str}

    --- BULLETS COVERING THE WHOLE ARTICLE ---
    {bullets}
    --- END BULLETS ---
    """).strip()

# -----------------------------
# Fallback (no-LLM) heuristics
# -----------------------------
def _fallback_from_fulltext(full_text: str) -> Dict[str, str]:
    """Heuristic fallback that never truncates mid-sentence; preserves versions."""
    clean = _filter_noise_text(full_text)
    if not clean:
        return {"tldr": "", "summary": ""}

    protected = _protect_versions(clean.replace("\n", " "))
    sents = [s.strip() for s in protected.split(".") if s.strip()]
    if not sents:
        return {"tldr": "", "summary": ""}

    long  = ". ".join(sents[:12]) + "."
    short = ". ".join(sents[:2])  + "."

    return {
        "tldr":    _normalize_whitespace(_restore_versions(short)),
        "summary": _normalize_whitespace(_restore_versions(long)),
    }

# -----------------------------
# Core LLM map-reduce (Anthropic Claude)
# -----------------------------
def _summarize_chunks_with_llm(chunks: List[str], title: Optional[str], url: Optional[str], lang_hint: Optional[str]) -> Dict[str, str]:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    full_text_for_fallback = "\n\n".join(chunks)

    if not api_key:
        return _fallback_from_fulltext(full_text_for_fallback)

    client = _anthropic_client()

    # 1) Map: turn each chunk into bullets
    bullets_all: List[str] = []
    for ch in chunks:
        backoff = 1.0
        ch = _filter_noise_text(ch)
        for attempt in range(4):
            try:
                resp = client.messages.create(
                    model=DEFAULT_MODEL,
                    max_tokens=512,
                    temperature=0.2,
                    system="You produce faithful, dense technical notes about Kubernetes and cloud-native technologies.",
                    messages=[
                        {"role": "user", "content": _prompt_chunk(title, url, lang_hint, ch)},
                    ],
                )
                bullets = (resp.content[0].text or "").strip()
                bullets = _strip_artifacts(_filter_noise_text(bullets))
                bullets_all.append(bullets)
                break
            except Exception:
                if attempt == 3:
                    bullets_all.append(f"- {ch[:800]}…")
                else:
                    time.sleep(backoff)
                    backoff *= 2.0

    joined_bullets = "\n".join(bullets_all)

    # 2) Reduce: synthesize final TL;DR + Summary
    backoff = 1.0
    for attempt in range(4):
        try:
            resp = client.messages.create(
                model=DEFAULT_MODEL,
                max_tokens=1024,
                temperature=0.2,
                system="Return STRICT JSON only — no prose, no markdown fences, no text before or after the JSON object.",
                messages=[
                    {"role": "user", "content": _prompt_reduce(title, url, lang_hint, joined_bullets)},
                ],
            )
            raw = (resp.content[0].text or "").strip()
            data = _extract_json(raw)

            if not data:
                raise ValueError(f"Could not parse JSON from response: {raw[:300]}")

            tldr    = _strip_artifacts(_filter_noise_text(str(data.get("tldr",    "")).strip()))
            summary = _strip_artifacts(_filter_noise_text(str(data.get("summary", "")).strip()))

            if not tldr or not summary:
                raise ValueError("Missing tldr or summary in model response.")

            return {
                "tldr":    _restore_versions(tldr),
                "summary": _restore_versions(summary),
            }
        except Exception:
            if attempt == 3:
                return _fallback_from_fulltext(full_text_for_fallback)
            time.sleep(backoff)
            backoff *= 2.0

# -----------------------------
# Public APIs
# -----------------------------
def generate_summaries_inline(
    article_text: str,
    title: Optional[str] = None,
    url: Optional[str] = None,
    lang_hint: Optional[str] = None,
    no_llm: bool = False,
) -> Dict[str, str]:
    """Summarize ALL of article_text via map-reduce."""
    text = (article_text or "").strip()
    if not text:
        return {"tldr": "", "summary": ""}

    text = _filter_noise_text(text)

    cache = _load_cache()
    key = _hash_key("inline", title or "", url or "", text, str(MAX_CHARS_PER_CHUNK))
    if key in cache:
        return cache[key]

    chunks = _split_into_chunks(text, MAX_CHARS_PER_CHUNK)

    result = _fallback_from_fulltext("\n\n".join(chunks)) if no_llm else \
             _summarize_chunks_with_llm(chunks, title, url, lang_hint)

    cache[key] = result
    _save_cache(cache)
    return result

def generate_summaries_from_url(
    url: str,
    title: Optional[str] = None,
    lang_hint: Optional[str] = None,
    no_llm: bool = False,
) -> Dict[str, str]:
    """Fetch URL, clean ALL content, summarize via map-reduce."""
    cache = _load_cache()
    key = _hash_key("url", title or "", url or "", str(MAX_CHARS_PER_CHUNK))
    if key in cache:
        return cache[key]

    full_text = fetch_full_text(url)
    if not full_text:
        result = {"tldr": "", "summary": ""}
        cache[key] = result
        _save_cache(cache)
        return result

    full_text = _filter_noise_text(full_text)
    chunks = _split_into_chunks(full_text, MAX_CHARS_PER_CHUNK)

    result = _fallback_from_fulltext("\n\n".join(chunks)) if no_llm else \
             _summarize_chunks_with_llm(chunks, title, url, lang_hint)

    cache[key] = result
    _save_cache(cache)
    return result
