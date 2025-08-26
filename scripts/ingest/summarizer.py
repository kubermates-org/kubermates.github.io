# scripts/ingest/summarizer.py
from __future__ import annotations
import os, json, time, hashlib, pathlib, textwrap
from typing import Dict, List, Optional

import requests
from bs4 import BeautifulSoup

# -----------------------------
# Config & cache
# -----------------------------
CACHE_PATH = pathlib.Path(".cache/summaries.json")
CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)

DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# Map-Reduce chunk size in characters (ensure full-page coverage)
# You can tune via env: SUMMARY_CHUNK_CHARS
MAX_CHARS_PER_CHUNK = int(os.getenv("SUMMARY_CHUNK_CHARS", "12000"))

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
    """Remove any leftover bullet/hash markers if a model misbehaves."""
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
    # Split by paragraphs, then pack
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

def _openai_client():
    from openai import OpenAI
    return OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# -----------------------------
# HTML fetch & clean
# -----------------------------
def _clean_html_to_text(html: str) -> str:
    if not html:
        return ""
    soup = BeautifulSoup(html, "html.parser")

    # strip non-content
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    root = soup.find("article") or soup.find("main") or soup.body or soup
    for tag in root.find_all(["nav", "footer", "aside"]):
        tag.decompose()

    paras = [p.get_text(" ", strip=True) for p in root.find_all("p")]
    text = "\n\n".join([p for p in paras if p]) or root.get_text(" ", strip=True)
    return textwrap.dedent(text).strip()

def fetch_full_text(url: str, timeout: int = 15) -> str:
    """Public: fetch and clean a page to plain text."""
    if not url:
        return ""
    try:
        headers = {"User-Agent": "Mozilla/5.0 (compatible; KubermatesBot/1.0; +https://kubermates.org)"}
        r = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)
        if r.status_code != 200 or not r.text:
            return ""
        return _clean_html_to_text(r.text)
    except Exception:
        return ""

# -----------------------------
# Prompts
# -----------------------------
def _prompt_chunk(title: Optional[str], url: Optional[str], lang_hint: Optional[str], chunk_text: str) -> str:
    meta = []
    if title: meta.append(f'Title: "{title}"')
    if url: meta.append(f"URL: {url}")
    if lang_hint: meta.append(f"Language hint: {lang_hint}")
    meta_str = "\n".join(meta)
    return textwrap.dedent(f"""
    You are summarizing ONE PART of a longer technical article. Read the chunk below and produce a concise bullet list of key facts ONLY from this chunk.

    Rules:
    - Write in the SAME LANGUAGE as the source text if clear; otherwise keep the language of the title or language hint.
    - Avoid fluff; capture key decisions, configs, APIs, versions, trade-offs, and outcomes.
    - Output PLAIN TEXT bullet points (use "- " per line). No markdown fences.

    {meta_str}

    --- CHUNK START ---
    {chunk_text}
    --- CHUNK END ---
    """).strip()

def _prompt_reduce(title: Optional[str], url: Optional[str], lang_hint: Optional[str], bullets: str) -> str:
    meta = []
    if title: meta.append(f'Title: "{title}"')
    if url: meta.append(f"URL: {url}")
    if lang_hint: meta.append(f"Language hint: {lang_hint}")
    meta_str = "\n".join(meta)
    return textwrap.dedent(f"""
    You are creating FINAL summaries from aggregated bullet points that cover ALL parts of the article.

    Output STRICT JSON with keys ONLY:
    "tldr": string  (about 1–2 sentences, target ~300 characters, ultra concise.)
    "summary": string (about 3–6 sentences, target ~1000 characters, crisp and complete.)

    Rules:
    - Keep the SAME LANGUAGE as the source (use the hint/title if needed).
    - Be faithful; use only information present in the bullets.
    - Prefer concrete details (versions, flags, concepts) over generic advice.
    - Do NOT include any list markers, section headers, or "# Chunk" text in either field.
    - Do NOT exceed the spirit of the targets; aim for readability without cutting mid-sentence.

    {meta_str}

    --- BULLETS COVERING THE WHOLE ARTICLE ---
    {bullets}
    --- END BULLETS ---
    """).strip()

# -----------------------------
# Fallback (no-LLM) heuristics
# -----------------------------
def _fallback_from_fulltext(full_text: str) -> Dict[str, str]:
    """Heuristic fallback that never truncates mid-sentence; aims near targets."""
    sents = [s.strip() for s in full_text.replace("\n", " ").split(".") if s.strip()]
    if not sents:
        return {"tldr": "", "summary": ""}

    # Build longer summary from first ~12 sentences (roughly ≈1000 chars in many tech texts)
    long = ". ".join(sents[:12]) + "."
    # TL;DR from first 1–2 sentences (~300 chars usually)
    short = ". ".join(sents[:2]) + "."

    return {"tldr": _normalize_whitespace(short), "summary": _normalize_whitespace(long)}

# -----------------------------
# Core LLM map-reduce
# -----------------------------
def _summarize_chunks_with_llm(chunks: List[str], title: Optional[str], url: Optional[str], lang_hint: Optional[str]) -> Dict[str, str]:
    api_key = os.getenv("OPENAI_API_KEY")
    full_text_for_fallback = "\n\n".join(chunks)

    if not api_key:
        return _fallback_from_fulltext(full_text_for_fallback)

    client = _openai_client()

    # 1) Map: turn each chunk into bullets
    bullets_all: List[str] = []
    for ch in chunks:
        backoff = 1.0
        for attempt in range(4):
            try:
                resp = client.chat.completions.create(
                    model=DEFAULT_MODEL,
                    temperature=0.2,
                    messages=[
                        {"role": "system", "content": "You produce faithful, dense technical notes."},
                        {"role": "user", "content": _prompt_chunk(title, url, lang_hint, ch)},
                    ],
                )
                bullets = resp.choices[0].message.content.strip()
                bullets_all.append(bullets)  # no "# Chunk" prefixes
                break
            except Exception:
                if attempt == 3:
                    # Graceful degrade: if a chunk fails, include raw slice
                    bullets_all.append(f"- {ch[:800]}…")
                else:
                    time.sleep(backoff)
                    backoff *= 2.0

    joined_bullets = "\n".join(bullets_all)

    # 2) Reduce: synthesize final TL;DR + Summary with character targets
    backoff = 1.0
    for attempt in range(4):
        try:
            resp = client.chat.completions.create(
                model=DEFAULT_MODEL,
                temperature=0.2,
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": "Return STRICT JSON only. Respect the character targets without truncating mid-sentence."},
                    {"role": "user", "content": _prompt_reduce(title, url, lang_hint, joined_bullets)},
                ],
            )
            raw = resp.choices[0].message.content
            data = json.loads(raw)

            tldr = _strip_artifacts(str(data.get("tldr", "")).strip())
            summary = _strip_artifacts(str(data.get("summary", "")).strip())

            if not tldr or not summary:
                raise ValueError("Missing keys in reduce result.")

            return {"tldr": tldr, "summary": summary}
        except Exception:
            if attempt == 3:
                # FINAL FALLBACK: summarize the full text, not the bullets
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
    """
    Summarize ALL of article_text via map-reduce. Character targets are handled in prompts only.
    """
    text = (article_text or "").strip()
    if not text:
        return {"tldr": "", "summary": ""}

    cache = _load_cache()
    key = _hash_key("inline", title or "", url or "", text, str(MAX_CHARS_PER_CHUNK))
    if key in cache:
        return cache[key]

    chunks = _split_into_chunks(text, MAX_CHARS_PER_CHUNK)

    if no_llm:
        result = _fallback_from_fulltext("\n\n".join(chunks))
    else:
        result = _summarize_chunks_with_llm(chunks, title, url, lang_hint)

    cache[key] = result
    _save_cache(cache)
    return result

def generate_summaries_from_url(
    url: str,
    title: Optional[str] = None,
    lang_hint: Optional[str] = None,
    no_llm: bool = False,
) -> Dict[str, str]:
    """
    Fetch URL, clean ALL content, summarize via map-reduce.
    """
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

    chunks = _split_into_chunks(full_text, MAX_CHARS_PER_CHUNK)

    if no_llm:
        result = _fallback_from_fulltext("\n\n".join(chunks))
    else:
        result = _summarize_chunks_with_llm(chunks, title, url, lang_hint)

    cache[key] = result
    _save_cache(cache)
    return result
