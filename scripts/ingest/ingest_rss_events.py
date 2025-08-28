#!/usr/bin/env python3
# scripts/ingest/ingest_rss_events.py
from __future__ import annotations

from datetime import datetime, timezone
import re

import feedparser
from bs4 import BeautifulSoup
from common import *  # load_sources, load_state, save_state, write_md, hash_id, already_seen, mark_seen, parse_date, slugify, CONTENT

# -----------------------------
# Output dir
# -----------------------------
OUT_DIR = CONTENT / "events"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Minimal Geo lookup (city → lat/lon, country → lat/lon)
# -----------------------------
CITY_CENTROIDS = {
    # AMER
    "new york": (40.7128, -74.0060), "san francisco": (37.7749, -122.4194),
    "seattle": (47.6062, -122.3321), "austin": (30.2672, -97.7431),
    "boston": (42.3601, -71.0589), "chicago": (41.8781, -87.6298),
    "los angeles": (34.0522, -118.2437), "mexico city": (19.4326, -99.1332),
    "toronto": (43.6532, -79.3832), "vancouver": (49.2827, -123.1207),
    "montreal": (45.5019, -73.5674), "sao paulo": (-23.5505, -46.6333),
    "rio de janeiro": (-22.9068, -43.1729),

    # EMEA
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

    # APAC
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
    # AMER
    "united states": (39.8283, -98.5795), "usa": (39.8283, -98.5795), "us": (39.8283, -98.5795),
    "canada": (56.1304, -106.3468), "mexico": (23.6345, -102.5528),
    "brazil": (-14.2350, -51.9253), "argentina": (-38.4161, -63.6167), "chile": (-35.6751, -71.5430),
    "colombia": (4.5709, -74.2973), "peru": (-9.1900, -75.0152),

    # EMEA
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

    # APAC
    "india": (20.5937, 78.9629), "china": (35.8617, 104.1954), "japan": (36.2048, 138.2529),
    "south korea": (35.9078, 127.7669), "korea, republic of": (35.9078, 127.7669),
    "singapore": (1.3521, 103.8198), "australia": (-25.2744, 133.7751),
    "new zealand": (-40.9006, 174.8860), "taiwan": (23.6978, 120.9605),
    "hong kong": (22.3193, 114.1694),
}

def _approx_coords(city: str | None, country: str | None, location: str | None) -> tuple[float | None, float | None]:
    """Return approximate (lat, lon) from city or country text."""
    def norm(x): return (x or "").strip().lower()
    cty, ctry = norm(city), norm(country)
    # Try "City, Country" in location when city missing
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

# -----------------------------
# Helpers
# -----------------------------
def clean_excerpt(html: str | None) -> str:
    """Return a short plain-text excerpt from feed HTML."""
    text = BeautifulSoup(html or "", "html.parser").get_text(" ", strip=True)
    return (text[:280] + "…") if len(text) > 280 else text

def write_event_md(fm: dict, title: str, start_dt: datetime, body: str = ""):
    fname = f"{start_dt.date()}-{slugify(title)}.md"
    write_md(OUT_DIR, fname, fm, body or (title[:300]))

def _parse_geo_from_entry(e) -> tuple[float | None, float | None]:
    """Try to extract (lat, lon) from common GeoRSS/Geo fields."""
    lat = lon = None

    # georss:point -> "LAT LON"
    pt = getattr(e, "georss_point", None) or e.get("georss_point")
    if isinstance(pt, str):
        parts = pt.split()
        if len(parts) == 2:
            try:
                lat, lon = float(parts[0]), float(parts[1])
            except Exception:
                pass

    # geo:lat / geo:long
    if lat is None:
        v = getattr(e, "geo_lat", None) or e.get("geo_lat")
        try:
            lat = float(v) if v is not None else None
        except Exception:
            lat = None
    if lon is None:
        v = getattr(e, "geo_long", None) or e.get("geo_long") or getattr(e, "geo_lon", None) or e.get("geo_lon")
        try:
            lon = float(v) if v is not None else None
        except Exception:
            lon = None

    return lat, lon

# -----------------------------
# Main
# -----------------------------
def run():
    # expects events RSS/Atom sources in data.yaml under "events"
    sources = load_sources().get("events", [])
    state = load_state()
    wrote = 0

    for s in sources:
        if s.get("type") not in ("rss", "atom"):
            continue

        feed = feedparser.parse(s["url"])
        for e in feed.entries[:80]:
            url = e.get("link") or e.get("id")
            if not url:
                continue

            uid = hash_id(url)
            if already_seen(state, uid):
                continue

            # Prefer published -> updated; if neither parsable, SKIP
            start = (
                parse_date(getattr(e, "published", None))
                or parse_date(getattr(e, "updated", None))
            )
            if not start:
                continue

            title = (e.get("title") or url).strip()

            # Basic text fields (if present in feeds)
            city = getattr(e, "city", None) or e.get("city")
            country = getattr(e, "country", None) or e.get("country")
            location = getattr(e, "location", None) or e.get("location")

            lat, lon = _parse_geo_from_entry(e)
            if lat is None or lon is None:
                # fallback to approximate from city/country
                lat2, lon2 = _approx_coords(city, country, location)
                lat = lat if lat is not None else lat2
                lon = lon if lon is not None else lon2

            # normalize country to lower (filters expect lower)
            country_norm = (country or None)
            if isinstance(country_norm, str):
                country_norm = country_norm.strip().lower() or None

            fm = {
                "title": title,
                "date": start.isoformat(),      # Hugo .Date
                "eventDate": start.isoformat(), # mirror
                "endDate": None,
                "location": location or None,
                "city": city or None,
                "country": country_norm,
                "region": None,
                "lat": lat,
                "lon": lon,
                "organizer": None,
                "mode": "online",
                "tags": ["event", s.get("category", "rss")],
                "source": s.get("name") or "rss",
                "external_url": url,
                "draft": False,
                "uid": uid,
                "provider": "rss",
            }

            body = clean_excerpt(getattr(e, "summary", "")) or title
            write_event_md(fm, title, start, body)
            mark_seen(state, uid, {"title": title, "date": start.isoformat(), "source": fm["source"]})
            wrote += 1

    save_state(state)
    print(f"[info] RSS wrote {wrote} new events")

if __name__ == "__main__":
    run()
