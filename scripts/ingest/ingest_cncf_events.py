#!/usr/bin/env python3
# scripts/ingest/ingest_events.py
from __future__ import annotations

import hashlib
import re
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import requests
from common import *  # load_state, save_state, write_md, hash_id, already_seen, mark_seen, parse_date, slugify, CONTENT

# -----------------------------
# Output dir
# -----------------------------
OUT_DIR = CONTENT / "events"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------
# CNCF (Bevy) public API
# -----------------------------
BEVY_URL = "https://community.cncf.io/api/search/?result_types=upcoming_event&country_code=Earth"

_DATE_ONLY_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# --- same lightweight lookup as RSS for consistent centroids ---
CITY_CENTROIDS = {
    "new york": (40.7128, -74.0060), "san francisco": (37.7749, -122.4194),
    "seattle": (47.6062, -122.3321), "austin": (30.2672, -97.7431),
    "boston": (42.3601, -71.0589), "chicago": (41.8781, -87.6298),
    "los angeles": (34.0522, -118.2437), "mexico city": (19.4326, -99.1332),
    "toronto": (43.6532, -79.3832), "vancouver": (49.2827, -123.1207),
    "montreal": (45.5019, -73.5674), "sao paulo": (-23.5505, -46.6333),
    "rio de janeiro": (-22.9068, -43.1729),

    "london": (51.5074, -0.1278), "paris": (48.8566, 2.3522),
    "berlin": (52.5200, 13.4050), "amsterdam": (52.3676, 4.9041),
    "dublin": (53.3498, -6.2603), "madrid": (40.4168, -3.7038),
    "barcelona": (41.3851, 2.1734), "lisbon": (38.7223, -9.1393),
    "stockholm": (59.3293, 18.0686), "oslo": (59.9139, 10.7522),
    "copenhagen": (55.6761, 12.5683), "helsinki": (60.1699, 24.9384),
    "zurich": (47.3769, 8.5417), "geneva": (46.2044, 6.1432),
    "prague": (50.0755, 14.4378), "vienna": (48.2082, 16.3738),
    "munich": (48.1351, 11.5820), "warsaw": (52.2297, 21.0122),
    "bucharest": (44.4268, 26.1025), "istanbul": (41.0082, 28.9784),
    "tel aviv": (32.0853, 34.7818), "dubai": (25.2048, 55.2708),
    "cape town": (-33.9249, 18.4241), "johannesburg": (-26.2041, 28.0473),

    "tokyo": (35.6762, 139.6503), "osaka": (34.6937, 135.5023),
    "seoul": (37.5665, 126.9780), "singapore": (1.3521, 103.8198),
    "shanghai": (31.2304, 121.4737), "beijing": (39.9042, 116.4074),
    "hong kong": (22.3193, 114.1694), "taipei": (25.0330, 121.5654),
    "sydney": (-33.8688, 151.2093), "melbourne": (-37.8136, 144.9631),
    "auckland": (-36.8485, 174.7633), "wellington": (-41.2866, 174.7756),
    "bangalore": (12.9716, 77.5946), "bengaluru": (12.9716, 77.5946),
    "hyderabad": (17.3850, 78.4867), "mumbai": (19.0760, 72.8777),
    "delhi": (28.6139, 77.2090),
}
COUNTRY_CENTROIDS = {
    "united states": (39.8283, -98.5795), "usa": (39.8283, -98.5795), "us": (39.8283, -98.5795),
    "canada": (56.1304, -106.3468), "mexico": (23.6345, -102.5528),
    "brazil": (-14.2350, -51.9253), "argentina": (-38.4161, -63.6167), "chile": (-35.6751, -71.5430),
    "colombia": (4.5709, -74.2973), "peru": (-9.1900, -75.0152),

    "united kingdom": (55.3781, -3.4360), "uk": (55.3781, -3.4360),
    "ireland": (53.1424, -7.6921), "france": (46.2276, 2.2137), "spain": (40.4637, -3.7492),
    "portugal": (39.3999, -8.2245), "germany": (51.1657, 10.4515), "netherlands": (52.1326, 5.2913),
    "belgium": (50.5039, 4.4699), "switzerland": (46.8182, 8.2275), "austria": (47.5162, 14.5501),
    "italy": (41.8719, 12.5674), "norway": (60.4720, 8.4689), "sweden": (60.1282, 18.6435),
    "finland": (61.9241, 25.7482), "denmark": (56.2639, 9.5018), "poland": (51.9194, 19.1451),
    "romania": (45.9432, 24.9668), "czechia": (49.8175, 15.4730), "czech republic": (49.8175, 15.4730),
    "israel": (31.0461, 34.8516), "turkey": (38.9637, 35.2433), "egypt": (26.8206, 30.8025),
    "united arab emirates": (23.4241, 53.8478), "uae": (23.4241, 53.8478),
    "south africa": (-30.5595, 22.9375),

    "india": (20.5937, 78.9629), "china": (35.8617, 104.1954), "japan": (36.2048, 138.2529),
    "south korea": (35.9078, 127.7669), "korea, republic of": (35.9078, 127.7669),
    "singapore": (1.3521, 103.8198), "australia": (-25.2744, 133.7751),
    "new zealand": (-40.9006, 174.8860), "taiwan": (23.6978, 120.9605),
    "hong kong": (22.3193, 114.1694),
}

def _approx_coords(city: str | None, country: str | None, location: str | None) -> tuple[float | None, float | None]:
    def norm(x): return (x or "").strip().lower()
    cty, ctry = norm(city), norm(country)
    if not cty and location:
        parts = [p.strip() for p in location.split(",") if p.strip()]
        if len(parts) >= 2:
            cty = parts[0].lower()
            ctry = parts[-1].lower()
    if cty and cty in CITY_CENTROIDS:
        return CITY_CENTROIDS[cty]
    if ctry and ctry in COUNTRY_CENTROIDS:
        return COUNTRY_CENTROIDS[ctry]
    return None, None

def _iso_utc_from_str(s: str | None) -> str | None:
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

def _cncf_pick_location(ev: dict):
    """
    Returns (location_str, city, country_lower, lat, lon)
    Pulls from venue/chapter and approximates coords if missing.
    """
    venue = ev.get("venue") or {}
    chap  = ev.get("chapter") or {}

    loc = (
        venue.get("address")
        or chap.get("chapter_location")
        or ev.get("location")
        or None
    )

    city = country = None
    if isinstance(loc, str) and "," in loc:
        parts = [p.strip() for p in loc.split(",") if p.strip()]
        if len(parts) >= 2:
            city = ", ".join(parts[:-1]) or None
            country = (parts[-1] or "").lower() or None

    # direct lat/lon if present
    def _num(x):
        try: return float(x)
        except Exception: return None

    lat = (
        _num((venue or {}).get("lat")) or _num((venue or {}).get("latitude")) or
        _num((chap or {}).get("lat"))  or _num((chap or {}).get("latitude"))
    )
    lon = (
        _num((venue or {}).get("lng")) or _num((venue or {}).get("lon")) or _num((venue or {}).get("longitude")) or
        _num((chap or {}).get("lng"))  or _num((chap or {}).get("lon"))  or _num((chap or {}).get("longitude"))
    )
    if lat is None and lon is None:
        latlng = (venue or {}).get("latlng") or (chap or {}).get("latlng")
        if isinstance(latlng, (list, tuple)) and len(latlng) == 2:
            lat, lon = _num(latlng[0]), _num(latlng[1])

    # fallback to approx from city/country
    if lat is None or lon is None:
        lat2, lon2 = _approx_coords(city, country, loc)
        lat = lat if lat is not None else lat2
        lon = lon if lon is not None else lon2

    return loc, city, (country or None), lat, lon

def _cncf_map_event(e: dict) -> dict:
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
        or f"https://community.cncf.io/events/{e.get('id','')}"
    )
    desc = (e.get("description_short") or e.get("description") or "").strip()
    loc, city, country, lat, lon = _cncf_pick_location(e)

    return {
        "title": title,
        "link": link,
        "eventDate": start,
        "endDate": end,
        "description": desc,
        "location": loc,
        "city": city,
        "country": country,
        "lat": lat,
        "lon": lon,
        "provider": "cncf",
        "source": "bevy-search-api",
        "tags": ["cncf", "event"],
        "uid": hashlib.sha256(("|".join([link or title, start or ""])).encode()).hexdigest()[:16],
    }

def fetch_cncf_events() -> list[dict]:
    r = requests.get(BEVY_URL, headers={"Accept": "application/json"}, timeout=30)
    r.raise_for_status()
    data = r.json()
    results = data.get("results") or []
    return [_cncf_map_event(e) for e in results if isinstance(e, dict)]

# -----------------------------
# Front matter & writer
# -----------------------------
def event_to_frontmatter(ev: dict):
    title = (ev.get("title") or "Kubernetes event").strip()
    start = parse_date(ev.get("eventDate")) if ev.get("eventDate") else None
    end = parse_date(ev.get("endDate")) if ev.get("endDate") else None
    link = (ev.get("link") or "").strip()

    # normalize country to lowercase for UI filtering
    country = ev.get("country") or None
    if isinstance(country, str):
        country = country.strip().lower() or None

    fm = {
        "title": title,
        "date": start.isoformat() if start else None,
        "endDate": end.isoformat() if end else None,
        "location": (ev.get("location") or "").strip() or None,
        "city": ev.get("city") or None,
        "country": country,
        "region": ev.get("region") or None,
        "lat": ev.get("lat") if ev.get("lat") is not None else None,
        "lon": ev.get("lon") if ev.get("lon") is not None else None,
        "organizer": ev.get("organizer") or None,
        "mode": "in-person" if ev.get("city") else "online",
        "tags": ["cncf", "event"],
        "source": "cncf-api",
        "external_url": link or None,
        "draft": False,
        "uid": ev.get("uid") or hash_id((link or title) + (start.isoformat() if start else "")),
        "provider": "cncf",
    }
    return fm, start, title

def write_event_md(fm: dict, title: str, start_dt: datetime, body: str = ""):
    fname = f"{start_dt.date()}-{slugify(title)}.md"
    write_md(OUT_DIR, fname, fm, body or (title[:300]))

# -----------------------------
# Main run
# -----------------------------
def run():
    state = load_state()
    wrote = 0

    try:
        events = fetch_cncf_events()
    except Exception as e:
        print(f"[warn] CNCF fetch failed: {e}")
        events = []

    for ev in events:
        start_dt = parse_date(ev.get("eventDate")) if ev.get("eventDate") else None
        if not start_dt:
            print(f"[warn] dropped event without valid start: {ev.get('title')}")
            continue

        uid = ev.get("uid")
        if not uid:
            base = (ev.get("link") or ev.get("title") or "") + ev.get("eventDate")
            uid = hash_id(base or repr(ev))
            ev["uid"] = uid

        if already_seen(state, uid):
            continue

        fm, _, title = event_to_frontmatter(ev)
        body = (ev.get("description") or ev.get("summary") or title)[:300]
        write_event_md(fm, title, start_dt, body)
        mark_seen(state, uid, {"title": title, "date": start_dt.isoformat(), "source": "cncf-api"})
        wrote += 1

    save_state(state)
    print(f"[info] CNCF wrote {wrote} new events")

if __name__ == "__main__":
    run()
