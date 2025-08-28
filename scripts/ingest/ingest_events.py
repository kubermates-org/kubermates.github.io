# ingest_events.py (self-contained)
from __future__ import annotations

import importlib
import importlib.util
import pathlib
import sys
import hashlib
import math
import re
from zoneinfo import ZoneInfo

import feedparser, requests
from bs4 import BeautifulSoup
from ics import Calendar
from datetime import datetime, timezone
from common import *

# ---- Config ----
PROVIDERS = [
    "kcds", "kubecon", "k8s_calendar",
    "platform_engineering",
    "aws", "azure", "gcp", "ovhcloud",
    "cncf_api",  # built-in Bevy API provider for CNCF community events
]

OUT_DIR = CONTENT / "events"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ---- Minimal helpers (no external geo dependency) ----
def bs_excerpt(html):
    text = BeautifulSoup(html or "", "html.parser").get_text(" ", strip=True)
    return (text or "")[:280]

def simple_enrich_location(loc: str):
    """
    Very lightweight parser: tries to extract (city, country) from a string like
    'City, Country'. Returns (city, country_lower, lat, lon, region) with empty
    lat/lon/region. Safe no-op if not parseable.
    """
    loc = (loc or "").strip()
    if not loc:
        return None, None, None, None, None
    parts = [p.strip() for p in loc.split(",") if p.strip()]
    if len(parts) >= 2:
        city = parts[0]
        country = parts[-1].lower()
        return city, country, None, None, None
    # Only one token -> assume city; no country
    return (parts[0], None, None, None, None) if parts else (None, None, None, None, None)

def normalize_geo(md: dict) -> dict:
    loc_hint = (md.get("location") or md.get("city") or "").strip()
    if loc_hint:
        city, country, lat, lon, region = simple_enrich_location(loc_hint)
        if city and not md.get("city"): md["city"] = city
        if country: md["country"] = country
        if region: md["region"] = region
        if lat is not None and lon is not None:
            md["lat"], md["lon"] = float(lat), float(lon)
    return md

def provider_event_to_frontmatter(ev: dict, source_name: str):
    title = (ev.get("title") or "Kubernetes event").strip()

    # IMPORTANT: do NOT fall back to "now" for provider events.
    start = parse_date(ev.get("eventDate")) if ev.get("eventDate") else None
    end = parse_date(ev.get("endDate")) if ev.get("endDate") else None
    link = (ev.get("link") or "").strip()

    ev = normalize_geo(ev)

    tags = set(ev.get("tags") or [])
    tags.add("event")
    if ev.get("provider"):
        tags.add(ev["provider"])
    tags_list = sorted(t for t in tags if t)

    fm = {
        "title": title,
        "date": start.isoformat() if start else None,
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
        "uid": ev.get("uid") or hash_id((link or title) + (start.isoformat() if start else "")),
        "provider": ev.get("provider") or None,
    }
    return fm, start, title

def write_event_md(fm: dict, title: str, start_dt: datetime, body: str = ""):
    fname = f"{start_dt.date()}-{slugify(title)}.md"
    write_md(OUT_DIR, fname, fm, body or (title[:300]))

# ---- RSS handler (unchanged logic) ----
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

# ---- iCal handler (unchanged logic) ----
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
        if fm["location"]:
            fm = normalize_geo(fm)
        body = (ev.description or title)[:300]
        write_event_md(fm, title, start, body)
        mark_seen(state, uid, {"title": title, "date": start.isoformat(), "source": source["name"]})

# ---- CNCF via Bevy Public API (built-in provider) ----
BEVY_BASE = "https://community.cncf.io"
BEVY_SEARCH = f"{BEVY_BASE}/api/search/"

_DATE_ONLY_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

def _iso_utc_from_str(s: str | None) -> str | None:
    """
    Normalize an incoming date/time string to ISO-8601 UTC.
    - If date-only (YYYY-MM-DD) => 'YYYY-MM-DDT00:00:00+00:00'
    - If ISO with tz => convert to UTC
    - If ISO naive => assume UTC
    """
    if not s:
        return None
    s = s.strip()
    if _DATE_ONLY_RE.match(s):
        return f"{s}T00:00:00+00:00"
    try:
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc).isoformat()
    except Exception:
        return None

def _iso_utc_from_local(s_local: str | None, tzname: str | None) -> str | None:
    """
    Convert a local naive ISO string with a tz name (e.g., 'Europe/Bucharest')
    into a UTC ISO string.
    """
    if not s_local or not tzname:
        return None
    try:
        dt_local = datetime.fromisoformat(s_local)
    except Exception:
        if _DATE_ONLY_RE.match(s_local):
            dt_local = datetime.fromisoformat(s_local + "T00:00:00")
        else:
            return None
    try:
        tz = ZoneInfo(tzname)
    except Exception:
        return None
    if dt_local.tzinfo is None:
        dt_local = dt_local.replace(tzinfo=tz)
    else:
        dt_local = dt_local.astimezone(tz)
    return dt_local.astimezone(timezone.utc).isoformat()

def _first(e: dict, *keys):
    for k in keys:
        v = e.get(k)
        if v is not None:
            return v
    return None

def _cncf_pick_location(ev: dict) -> tuple[str | None, str | None, str | None]:
    # Prefer venue address; fallback to chapter location
    loc = (
        (ev.get("venue") or {}).get("address")
        or (ev.get("chapter") or {}).get("chapter_location")
        or ev.get("location")
        or None
    )
    city = country = None
    if isinstance(loc, str) and "," in loc:
        parts = [p.strip() for p in loc.split(",")]
        if len(parts) >= 2:
            city = ", ".join(parts[:-1]) or None
            country = (parts[-1] or "").lower() or None
    return loc, city, country

def _cncf_map_event(e: dict) -> dict:
    """
    Build our normalized event dict with robust date picking.
    Preferred order:
      1) start_time_utc / end_time_utc
      2) start_time / end_time (tz-aware)
      3) start_time_local + timezone
      4) start_date / end_date (date-only)
    """
    title = (e.get("title") or "CNCF Event").strip()
    tzname = _first(e, "timezone", "time_zone", "timeZone")

    start = (
        _iso_utc_from_str(_first(e, "start_time_utc"))
        or _iso_utc_from_str(_first(e, "start_time"))
        or _iso_utc_from_local(_first(e, "start_time_local"), tzname)
        or _iso_utc_from_str(_first(e, "start_datetime", "startDateTime", "start"))
        or _iso_utc_from_str(_first(e, "start_date", "startDate"))
    )

    end = (
        _iso_utc_from_str(_first(e, "end_time_utc"))
        or _iso_utc_from_str(_first(e, "end_time"))
        or _iso_utc_from_local(_first(e, "end_time_local"), tzname)
        or _iso_utc_from_str(_first(e, "end_datetime", "endDateTime", "end"))
        or _iso_utc_from_str(_first(e, "end_date", "endDate"))
    )

    link = (
        e.get("public_url")
        or e.get("event_url")
        or e.get("url")
        or f"{BEVY_BASE}/events/{e.get('id','')}"
    )
    desc = (e.get("description_short") or e.get("description") or "").strip()
    loc, city, country = _cncf_pick_location(e)

    return {
        "title": title,
        "link": link,
        "eventDate": start,
        "endDate": end,
        "description": desc,
        "location": loc,
        "city": city,
        "country": country,
        "provider": "cncf",
        "source": "bevy-search-api",
        "tags": ["cncf", "event"],
        "uid": hashlib.sha256(("|".join([link or title, start or ""])).encode()).hexdigest()[:16],
    }

def fetch_cncf_api(session: requests.Session) -> list[dict]:
    """
    Calls the Bevy public search API for all upcoming CNCF events.
    Endpoint: /api/search/?result_types=upcoming_event&country_code=Earth
    """
    headers = {"Accept": "application/json"}
    params = {
        "result_types": "upcoming_event",
        "country_code": "Earth",
        "page": 1,
    }
    out = []

    r = session.get(BEVY_SEARCH, params=params, headers=headers, timeout=30)
    r.raise_for_status()
    data = r.json()
    results = data.get("results") or []
    out.extend(_cncf_map_event(e) for e in results if isinstance(e, dict))

    total = data.get("total") or len(results)
    per_page = data.get("per_page") or data.get("page_size") or len(results) or 1
    pages = data.get("total_pages") or (math.ceil(total / per_page) if per_page else 1)

    for page in range(2, int(pages) + 1):
        params["page"] = page
        r = session.get(BEVY_SEARCH, params=params, headers=headers, timeout=30)
        r.raise_for_status()
        data = r.json()
        results = data.get("results") or []
        out.extend(_cncf_map_event(e) for e in results if isinstance(e, dict))

    return out

# Registry of built-in providers (resolved before dynamic imports)
INTERNAL_PROVIDERS = {
    "cncf_api": fetch_cncf_api,
}

# ---- Provider loader that works with or without packages ----
def _resolve_fetch_fn(name: str):
    # 1) built-ins
    if name in INTERNAL_PROVIDERS:
        return INTERNAL_PROVIDERS[name]

    # 2) try as a package import (legacy layout)
    try:
        mod = importlib.import_module(f"scripts.events.providers.{name}")
        fn = getattr(mod, "fetch", None)
        if callable(fn):
            return fn
    except Exception:
        pass

    # 3) try loading directly from a file path (no packages needed)
    here = pathlib.Path(__file__).resolve().parent               # scripts/ingest/
    candidates = [
        here.parent / "events" / "providers" / f"{name}.py",     # scripts/events/providers/name.py
        pathlib.Path.cwd() / "scripts" / "events" / "providers" / f"{name}.py",
        here / "providers" / f"{name}.py",                       # scripts/ingest/providers/name.py (fallback)
    ]
    for p in candidates:
        if p.exists():
            spec = importlib.util.spec_from_file_location(f"prov_{name}", str(p))
            mod = importlib.util.module_from_spec(spec)
            assert spec and spec.loader, f"Cannot load spec for provider {name}"
            spec.loader.exec_module(mod)  # type: ignore[attr-defined]
            fn = getattr(mod, "fetch", None)
            if callable(fn):
                return fn

    # 4) nothing worked
    raise ImportError(f"provider '{name}' not found at package or file path")

# ---- Providers handler (checks built-ins first; SKIPS events without a valid start) ----
def handle_providers(state):
    seen_count = 0
    session = requests.Session()
    for name in PROVIDERS:
        try:
            fetch_fn = _resolve_fetch_fn(name)
        except Exception as e:
            print(f"[info] skipping provider {name}: {e}")
            continue

        try:
            events = fetch_fn(session)
        except Exception as e:
            print(f"[warn] provider {name} fetch failed: {e}")
            continue

        for ev in events:
            # ensure there is a parsable start; if missing -> skip (NO 'now' fallback)
            start_dt = parse_date(ev.get("eventDate")) if ev.get("eventDate") else None
            if not start_dt:
                print(f"[warn] provider {name} dropped event without valid start: {ev.get('title')}")
                continue

            candidate_uid = ev.get("uid")
            if not candidate_uid:
                base = (ev.get("link") or ev.get("title") or "") + ev.get("eventDate")
                candidate_uid = hash_id(base or repr(ev))
                ev["uid"] = candidate_uid

            if already_seen(state, candidate_uid):
                continue

            fm, _, title = provider_event_to_frontmatter(ev, source_name=name)
            body = (ev.get("description") or ev.get("summary") or title)[:300]
            write_event_md(fm, title, start_dt, body)
            mark_seen(state, candidate_uid, {"title": title, "date": start_dt.isoformat(), "source": name})
            seen_count += 1

    print(f"[info] Providers wrote {seen_count} new events")

# ---- Entry point ----
def run():
    sources = load_sources().get("events", [])
    state = load_state()

    # 1) Providers first (upcoming curated feeds)
    handle_providers(state)

    # 2) RSS and 3) iCal
    for s in sources:
        if s.get("type") == "rss":
            handle_rss(s, state)
        elif s.get("type") == "ical":
            handle_ical(s, state)

    save_state(state)

if __name__ == "__main__":
    run()
