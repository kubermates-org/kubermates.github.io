# ingest_events.py
import importlib
import pathlib
import feedparser, requests
from bs4 import BeautifulSoup
from ics import Calendar
from datetime import datetime, timezone
from common import *
from scripts.events.geo import enrich_location  # reuses your enrich fn

# ---- Config ----
PROVIDERS = [
    "kcds", "kubecon", "k8s_calendar",
    "platform_engineering",
    "aws", "azure", "gcp", "ovhcloud",
]

OUT_DIR = CONTENT / "events"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ---- Helpers ----
def bs_excerpt(html):
    text = BeautifulSoup(html or "", "html.parser").get_text(" ", strip=True)
    return (text or "")[:280]

def normalize_geo(md: dict) -> dict:
    # Try to enrich from 'location' then fallback to 'city'
    loc_hint = (md.get("location") or md.get("city") or "").strip()
    if loc_hint:
        city, country, lat, lon, region = enrich_location(loc_hint)
        if city and not md.get("city"): md["city"] = city
        if country: md["country"] = country.lower()
        if region: md["region"] = region
        if lat and lon:
            md["lat"], md["lon"] = float(lat), float(lon)
    return md

def provider_event_to_frontmatter(ev: dict, source_name: str):
    """
    Map provider event dict -> front matter dict used by write_md()
    Expected provider keys (best-effort): title, eventDate, endDate, location, city,
      country, region, lat, lon, link, source, provider, uid, tags, organizer, mode
    """
    # Defaults / fallbacks
    title = (ev.get("title") or "Kubernetes event").strip()
    start = parse_date(ev.get("eventDate")) or datetime.now(timezone.utc)
    end = parse_date(ev.get("endDate")) if ev.get("endDate") else None
    link = (ev.get("link") or "").strip()

    # Enrich geo if we can
    ev = normalize_geo(ev)

    tags = set(ev.get("tags") or [])
    # Ensure generic + category/provider tags exist
    tags.add("event")
    if ev.get("provider"):
        tags.add(ev["provider"])
    # Source category if any (keeps parity with RSS/ICAL)
    # (We keep "event" + possibly a provider key; site templates can filter by either.)
    tags_list = sorted(t for t in tags if t)

    fm = {
        "title": title,
        "date": start.isoformat(),
        "endDate": end.isoformat() if end else None,
        "location": (ev.get("location") or "").strip() or None,
        "city": ev.get("city") or None,
        "country": ev.get("country") or None,
        "region": ev.get("region") or None,
        "lat": ev.get("lat") if ev.get("lat") is not None else None,
        "lon": ev.get("lon") if ev.get("lon") is not None else None,
        "organizer": ev.get("organizer") or None,
        "mode": ev.get("mode") or ("in-person" if ev.get("city") else "online"),
        "tags": tags_list,
        "source": ev.get("source") or source_name,
        "external_url": link or None,
        "draft": False,
        # Keep uid in the file to help downstream/template logic if needed
        "uid": ev.get("uid") or hash_id((link or title) + start.isoformat()),
        "provider": ev.get("provider") or None,
    }
    return fm, start, title

def write_event_md(fm: dict, title: str, start_dt: datetime, body: str = ""):
    # File name consistent with existing RSS/ICAL write: <YYYY-MM-DD>-<slug>.md
    fname = f"{start_dt.date()}-{slugify(title)}.md"
    write_md(OUT_DIR, fname, fm, body or (title[:300]))

# ---- Existing handlers (unchanged) ----
def handle_rss(source, state):
    feed = feedparser.parse(source["url"])
    for e in feed.entries[:50]:
        url = e.get("link") or e.get("id")
        title = e.get("title", " ").strip() or url
        if not url:
            continue
        uid = hash_id(url)
        if already_seen(state, uid):
            continue
        start = parse_date(getattr(e, "published", None)) or datetime.now(timezone.utc)
        fm = {
            "title": title,
            "date": start.isoformat(),
            "endDate": None,
            "location": None,
            "city": None,
            "country": None,
            "region": None,
            "lat": None,
            "lon": None,
            "organizer": None,
            "mode": "online",
            "tags": ["event", source.get("category","event")],
            "source": source["name"],
            "external_url": url,
            "draft": False,
            "uid": uid,
            "provider": None,
        }
        body = bs_excerpt(getattr(e, "summary","")) or title
        write_event_md(fm, title, start, body)
        mark_seen(state, uid, {"title": title, "date": start.isoformat(), "source": source["name"]})

def handle_ical(source, state):
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
        # Build base FM
        fm = {
            "title": title,
            "date": start.isoformat(),
            "endDate": end.isoformat() if end else None,
            "location": (ev.location or "").strip() or None,
            "city": None,
            "country": None,
            "region": None,
            "lat": None,
            "lon": None,
            "organizer": None,
            "mode": "in-person" if (ev.location or "").strip() else "online",
            "tags": ["event", source.get("category","event")],
            "source": source["name"],
            "external_url": url or source["url"],
            "draft": False,
            "uid": uid,
            "provider": None,
        }
        # Geo enrich from location if present
        if fm["location"]:
            fm = normalize_geo(fm)
        body = (ev.description or title)[:300]
        write_event_md(fm, title, start, body)
        mark_seen(state, uid, {"title": title, "date": start.isoformat(), "source": source["name"]})

# ---- New: Providers handler ----
def handle_providers(state):
    seen_count = 0
    for name in PROVIDERS:
        try:
            mod = importlib.import_module(f"scripts.events.providers.{name}")
        except Exception as e:
            print(f"[warn] provider {name} import failed: {e}")
            continue

        try:
            events = mod.fetch(requests.Session())
        except Exception as e:
            print(f"[warn] provider {name} fetch failed: {e}")
            continue

        for ev in events:
            # Prefer provider-supplied uid; otherwise build a stable one
            candidate_uid = ev.get("uid")
            if not candidate_uid:
                # Build from link/title + date to keep stability
                base = (ev.get("link") or ev.get("title") or "") + (ev.get("eventDate") or "")
                candidate_uid = hash_id(base or repr(ev))
                ev["uid"] = candidate_uid

            if already_seen(state, candidate_uid):
                continue

            # Normalize + write
            fm, start_dt, title = provider_event_to_frontmatter(ev, source_name=name)
            body = (ev.get("description") or ev.get("summary") or title)[:300]
            write_event_md(fm, title, start_dt, body)

            # Mark seen
            mark_seen(state, candidate_uid, {"title": title, "date": start_dt.isoformat(), "source": name})
            seen_count += 1

    print(f"[info] Providers wrote {seen_count} new events")

# ---- Entry point ----
def run():
    sources = load_sources().get("events", [])
    state = load_state()

    # 1) Providers (new upcoming events)
    handle_providers(state)

    # 2) RSS + 3) iCal (existing)
    for s in sources:
        if s.get("type") == "rss":
            handle_rss(s, state)
        elif s.get("type") == "ical":
            handle_ical(s, state)

    save_state(state)

if __name__ == "__main__":
    run()
