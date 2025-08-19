import feedparser, requests
from bs4 import BeautifulSoup
from ics import Calendar
from datetime import datetime, timezone
from common import *

def bs_excerpt(html):
    text = BeautifulSoup(html or "", "html.parser").get_text(" ", strip=True)
    return (text or "")[:280]

def handle_rss(source, state, outdir):
    feed = feedparser.parse(source["url"])
    for e in feed.entries[:50]:
        url = e.get("link") or e.get("id")
        title = e.get("title"," ").strip() or url
        if not url:
            continue
        uid = hash_id(url)
        if already_seen(state, uid):
            continue
        start = parse_date(getattr(e, "published", None)) or datetime.now(timezone.utc)
        fm = {
            "title": title,
            "date": start.isoformat(),
            "tags": ["event", source.get("category","event")],
            "source": source["name"],
            "external_url": url,
            "draft": False
        }
        body = bs_excerpt(getattr(e, "summary","")) or title
        write_md(outdir, f"{start.date()}-{slugify(title)}.md", fm, body)
        mark_seen(state, uid, {"title": title, "date": start.isoformat(), "source": source["name"]})

def handle_ical(source, state, outdir):
    text = requests.get(source["url"], timeout=30).text
    cal = Calendar(text)
    for ev in cal.events:
        url = (ev.url or "")[:500]
        title = (ev.name or "Kubernetes event").strip()
        uid = hash_id((url or title) + str(ev.begin))
        if already_seen(state, uid):
            continue
        start = ev.begin.datetime if ev.begin else datetime.now(timezone.utc)
        end = ev.end.datetime if ev.end else None
        fm = {
            "title": title,
            "date": start.isoformat(),
            "endDate": end.isoformat() if end else None,
            "location": (ev.location or "").strip() or None,
            "tags": ["event", source.get("category","event")],
            "source": source["name"],
            "external_url": url or source["url"],
            "draft": False
        }
        body = (ev.description or title)[:300]
        write_md(outdir, f"{start.date()}-{slugify(title)}.md", fm, body)
        mark_seen(state, uid, {"title": title, "date": start.isoformat(), "source": source["name"]})

def run():
    sources = load_sources().get("events", [])
    state = load_state()
    outdir = CONTENT / "events"
    for s in sources:
        if s["type"] == "rss":
            handle_rss(s, state, outdir)
        elif s["type"] == "ical":
            handle_ical(s, state, outdir)
    save_state(state)

if __name__ == "__main__":
    run()
