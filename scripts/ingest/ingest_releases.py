# scripts/ingest/ingest_releases.py
import feedparser
from bs4 import BeautifulSoup
from datetime import datetime, timezone

from common import (  # your existing utils
    load_sources, load_state, save_state,
    write_md, hash_id, already_seen, mark_seen,
    parse_date, slugify, CONTENT
)

from summarizer import generate_summaries_from_url, fetch_full_text


def clean_excerpt(html: str) -> str:
    """Short plain-text excerpt from feed HTML (fallback/optional)."""
    text = BeautifulSoup(html or "", "html.parser").get_text(" ", strip=True)
    text = text or ""
    return (text[:280] + "…") if len(text) > 280 else text


def run():
    sources = load_sources().get("releases", [])
    state = load_state()
    outdir = CONTENT / "releases"

    for s in sources:
        feed = feedparser.parse(s["url"])
        for e in feed.entries[:50]:
            url = e.get("link") or e.get("id")
            title = (e.get("title", "") or "").strip() or url
            if not url:
                continue

            uid = hash_id(url)
            if already_seen(state, uid):
                continue

            date = (
                parse_date(getattr(e, "published", None))
                or parse_date(getattr(e, "updated", None))
                or datetime.now(timezone.utc)
            )

            # Optional: quick excerpt from feed (not stored — useful if you later want a preview)
            _ = clean_excerpt(getattr(e, "summary", "") or "")

            # Fetch full cleaned text (to detect empty/ultra-short releases)
            full_text = fetch_full_text(url)

            # If page is empty/very short, skip LLM and keep blank summaries (prevents odd outputs)
            if not full_text or len(full_text.strip()) < 80:
                summ = {"tldr": "", "summary": ""}
            else:
                summ = generate_summaries_from_url(
                    url=url,
                    title=title,
                    lang_hint=None,   # set "en"/"fr" if you detect language elsewhere
                    no_llm=False,     # set True locally to skip API usage and use fallback
                )

            fm = {
                "title": title,
                "date": date.isoformat(),
                "tags": s.get("tags", []),
                "source": s["name"],
                "external_url": url,
                "post_kind": "release",
                "draft": False,
                "tldr": summ.get("tldr", ""),
                "summary": summ.get("summary", ""),
            }

            # Keep body empty to match your current site behavior.
            filename = f"{date.date()}-{slugify(title)}.md"
            write_md(outdir, filename, fm, body="")

            mark_seen(state, uid, {
                "title": title,
                "date": date.isoformat(),
                "source": s["name"],
            })

    save_state(state)


if __name__ == "__main__":
    run()
