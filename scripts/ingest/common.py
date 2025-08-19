import hashlib, os, re, json, pathlib, yaml, sys
from dateutil import parser as dtp

ROOT = pathlib.Path(__file__).resolve().parents[2]  # repo root
CONTENT = ROOT / "content"
DATA = ROOT / "data"
STATE = ROOT / "scripts" / "ingest" / "state.json"

def load_sources():
    with open(DATA / "sources.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def load_state():
    if STATE.exists():
        return json.loads(STATE.read_text())
    return {"seen": {}}

def save_state(state):
    STATE.write_text(json.dumps(state, indent=2, ensure_ascii=False))

def slugify(title):
    s = re.sub(r"[^a-z0-9]+", "-", (title or "").lower())
    return s.strip("-")[:80] or "post"

def hash_id(url_or_title):
    return hashlib.sha1((url_or_title or "").encode("utf-8")).hexdigest()[:12]

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def write_md(dirpath, filename, front_matter, body=""):
    ensure_dir(dirpath)
    p = dirpath / filename
    fm = yaml.safe_dump(front_matter, allow_unicode=True, sort_keys=False).strip()
    safe_body = (body or "").strip()
    if not safe_body:
        url = front_matter.get("external_url") or ""
        safe_body = f"Open the original post ↗ {url}".strip()
    content = f"---\n{fm}\n---\n{safe_body}\n"
    p.write_text(content, encoding="utf-8")
    print(f"[write] {p.relative_to(ROOT)}", file=sys.stderr)
    return p

def parse_date(d):
    if not d: return None
    try:
        return dtp.parse(d)
    except Exception:
        return None

def already_seen(state, uid):
    return uid in state["seen"]

def mark_seen(state, uid, meta):
    state["seen"][uid] = {
        "title": meta.get("title"),
        "date": meta.get("date"),
        "source": meta.get("source"),
    }
