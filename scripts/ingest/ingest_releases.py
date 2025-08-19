import feedparser
from bs4 import BeautifulSoup
from datetime import datetime, timezone
from common import *

def run():
    sources = load_sources().get("releases", [])
    state = load_state()
    outdir = CONTENT / "releases"

    for s in sources:
        feed = feedparser.parse(s["url"])
        for e in feed.entries[:50]:
            url = e.get("link") or e.get("id")
            title = e.get("title", "").strip() or url
            if not url:
                continue
            uid = hash_id(url)
            if already_seen(state, uid):
                continue
            date = parse_date(getattr(e, "published", None)) or parse_date(getattr(e, "updated", None)) or datetime.now(timezone.utc)

            fm = {
                "title": title,
                "date": date.isoformat(),
                "tags": s.get("tags", []),
                "source": s["name"],
                "external_url": url,
                "post_kind": "release",
                "draft": False,
            }
            filename = f"{date.date()}-{slugify(title)}.md"
            write_md(outdir, filename, fm, body="")
            mark_seen(state, uid, {"title": title, "date": date.isoformat(), "source": s["name"]})

    save_state(state)

if __name__ == "__main__":
    run()
