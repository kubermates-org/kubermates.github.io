# scripts/ingest/ingest_docs.py
import feedparser
from datetime import datetime, timezone
from common import *  # load_sources, load_state, save_state, write_md, hash_id, already_seen, mark_seen, parse_date, slugify, CONTENT
from summarizer import generate_summaries_from_url


def run():
    sources = load_sources().get("docs", [])
    state = load_state()
    outdir = CONTENT / "docs"

    for s in sources:
        try:
            feed = feedparser.parse(s["url"])
        except Exception as exc:
            print(f"[warn] docs: failed to fetch feed {s.get('name')} ({s['url']}): {exc}", file=sys.stderr)
            continue

        for e in feed.entries[:50]:
            try:
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
            except Exception as exc:
                print(f"[warn] docs: skipping entry '{e.get('title', url)}' from {s.get('name')}: {exc}", file=sys.stderr)

    save_state(state)


if __name__ == "__main__":
    run()
