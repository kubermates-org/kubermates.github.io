#!/usr/bin/env python3
"""
Fetch events (dummy examples), enrich with geo, and write Hugo content files.
Run from repo root:  python scripts/events/fetch_events.py
"""
import sys
from pathlib import Path
from typing import Dict, Any

# Ensure we can import scripts.events.geo when run directly
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from scripts.events.geo import enrich_location  # noqa

OUT_DIR = ROOT / "content" / "events"
OUT_DIR.mkdir(parents=True, exist_ok=True)

def fetch_sample_events():
    # Two sample events to prove rendering & map markers
    return [
        {
            "uid": "kubecon-eu-2026",
            "title": 'KubeCon + CloudNativeCon Europe 2026',
            "eventDate": "2026-03-10T09:00:00+01:00",
            "endDate": "2026-03-13T18:00:00+01:00",
            "location": "Paris, France",
            "organizer": "CNCF",
            "link": "https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/",
            "source": "cncf",
            "provider": "cncf",
            "mode": "in-person",
            "tags": ["kubernetes","cncf"]
        },
        {
            "uid": "platformcon-2026",
            "title": "PlatformCon 2026",
            "eventDate": "2026-06-10T09:00:00+01:00",
            "location": "London, United Kingdom",
            "organizer": "Platform Engineering",
            "link": "https://platformcon.com/",
            "source": "platform",
            "provider": "platform",
            "mode": "in-person",
            "tags": ["platform-engineering","devops"]
        },
    ]

def normalize_event(md: Dict[str, Any]) -> Dict[str, Any]:
    city, country, lat, lon, region = enrich_location(
        md.get("location", "") or md.get("city", "")
    )
    if city and not md.get("city"): md["city"] = city
    if country: md["country"] = country.lower()
    if region: md["region"] = region
    if lat and lon:
        md["lat"], md["lon"] = float(lat), float(lon)

    md.setdefault("provider", md.get("source", "cncf"))
    md.setdefault("mode", "in-person" if md.get("city") else "online")
    md.setdefault("tags", [])
    return md

def write_event(md: Dict[str, Any]):
    md = normalize_event(md)
    slug = md["uid"]
    p = OUT_DIR / f"{slug}.md"

    tags_str = ", ".join([f'"{t}"' for t in md.get("tags", [])])
    safe_title = (md["title"] or "").replace('"', "'")

    lines = [
        "---",
        f'title: "{safe_title}"',
        f"eventDate: {md['eventDate']}",
    ]
    if md.get("endDate"):
        lines.append(f"endDate: {md['endDate']}")
    if md.get("location"):
        lines.append(f'location: "{md["location"]}"')
    lines.append(f'provider: "{md.get("provider","")}"')
    lines.append(f'mode: "{md.get("mode","")}"')
    if md.get("region"):
        lines.append(f'region: "{md["region"]}"')
    if md.get("country"):
        lines.append(f'country: "{md["country"]}"')
    if md.get("city"):
        lines.append(f'city: "{md["city"]}"')
    if md.get("lat") and md.get("lon"):
        lines.append(f"lat: {md['lat']}")
        lines.append(f"lon: {md['lon']}")
    if md.get("organizer"):
        lines.append(f'organizer: "{md["organizer"]}"')
    if md.get("link"):
        lines.append(f'link: "{md["link"]}"')
    lines.append(f'source: "{md.get("source","")}"')
    lines.append(f'uid: "{md["uid"]}"')
    lines.append(f"tags: [{tags_str}]")
    lines.append("draft: false")
    lines.append("---")
    content = "\n".join(lines) + "\n"
    p.write_text(content, encoding="utf-8")
    print(f"✅ wrote {p}")

def main():
    for ev in fetch_sample_events():
        write_event(ev)

if __name__ == "__main__":
    main()
