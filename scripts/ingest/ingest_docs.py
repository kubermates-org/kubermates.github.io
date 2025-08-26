# scripts/ingest/ingest_docs.py
import feedparser
from bs4 import BeautifulSoup
from datetime import datetime, timezone
from common import *  # load_sources, load_state, save_state, write_md, hash_id, already_seen, mark_seen, parse_date, slugify, CONTENT
from summarizer import generate_summaries_from_url, fetch_full_text


def clean_excerpt(html):
    """Extract a short plain-text excerpt from feed HTML (fallback)."""
    text = BeautifulSoup(html or "", "html.parser").get_text(" ", strip=True)
    text = text or ""
    return (text[:280] + "…") if len(text) > 280 else text


def run():
    sources = load_sources().get("docs", [])
    state = load_state()
    outdir = CONTENT / "docs"

    for s in sources:
        feed = feedparser.parse(s["url"])
        for e in feed.entries[:50]:
            url = e.get("link") or e.get("id")
            title = (e.get("title", "") or "").strip() or url
            if not url:
                continue

            # Optional keyword filter per source
            flt = s.get("filter")
            hay = (title + " " + (getattr(e, "summary", "") or "")).lower()
            if flt and flt.lower() not in hay:
                continue

            uid = hash_id(url)
            if already_seen(state, uid):
                continue

            date = (
                parse_date(getattr(e, "published", None))
                or parse_date(getattr(e, "updated", None))
                or datetime.now(timezone.utc)
            )

            # Optional: fetch full cleaned text (not stored here, but you may want it later)
            _ = fetch_full_text(url)
            feed_excerpt = clean_excerpt(getattr(e, "summary", "") or "")

            # Generate final TL;DR + Summary over the FULL article (map-reduce)
            summ = generate_summaries_from_url(
                url=url,
                title=title,
                lang_hint=None,   # pass "en"/"fr" if you detect it elsewhere
                no_llm=False,     # set True locally to skip API usage
            )

            fm = {
                "title": title,
                "date": date.isoformat(),
                "tags": s.get("tags", []),
                "source": s["name"],
                "external_url": url,
                "post_kind": "link",
                "draft": False,
                "tldr": summ.get("tldr", ""),
                "summary": summ.get("summary", ""),
            }

            # Keep body empty as in your current setup
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
