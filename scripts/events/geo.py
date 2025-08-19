import re
from typing import Optional, Tuple

COUNTRY_REGION = {
    "FR":"eu","DE":"eu","NL":"eu","BE":"eu","LU":"eu","CH":"eu","AT":"eu","IT":"eu","ES":"eu","PT":"eu",
    "GB":"eu","IE":"eu","DK":"eu","NO":"eu","SE":"eu","FI":"eu","PL":"eu","CZ":"eu","SK":"eu","HU":"eu",
    "RO":"eu","BG":"eu","GR":"eu","SI":"eu","HR":"eu","EE":"eu","LV":"eu","LT":"eu","IS":"eu","MT":"eu",
    "US":"na","CA":"na","MX":"na",
    "BR":"latam","AR":"latam","CL":"latam","CO":"latam","PE":"latam",
    "JP":"apac","KR":"apac","CN":"apac","SG":"apac","AU":"apac","NZ":"apac","IN":"apac","ID":"apac","PH":"apac",
    "MY":"apac","TH":"apac","TW":"apac","HK":"apac","VN":"apac",
    "AE":"mea","SA":"mea","QA":"mea","IL":"mea","TR":"mea","EG":"mea","MA":"mea","ZA":"mea","KE":"mea","NG":"mea",
}

CITY_DB = {
    # EU
    "paris, fr": (48.8566, 2.3522), "london, gb": (51.5074, -0.1278), "berlin, de": (52.5200, 13.4050),
    "munich, de": (48.1372, 11.5756), "frankfurt, de": (50.1109, 8.6821), "amsterdam, nl": (52.3676, 4.9041),
    "brussels, be": (50.8503, 4.3517), "dublin, ie": (53.3498, -6.2603), "copenhagen, dk": (55.6761, 12.5683),
    "oslo, no": (59.9139, 10.7522), "stockholm, se": (59.3293, 18.0686), "helsinki, fi": (60.1699, 24.9384),
    "madrid, es": (40.4168, -3.7038), "barcelona, es": (41.3851, 2.1734), "lisbon, pt": (38.7223, -9.1393),
    "rome, it": (41.9028, 12.4964), "milan, it": (45.4642, 9.1900), "vienna, at": (48.2082, 16.3738),
    "prague, cz": (50.0755, 14.4378), "warsaw, pl": (52.2297, 21.0122), "budapest, hu": (47.4979, 19.0402),
    # NA
    "new york, us": (40.7128, -74.0060), "boston, us": (42.3601, -71.0589), "chicago, us": (41.8781, -87.6298),
    "austin, us": (30.2672, -97.7431), "seattle, us": (47.6062, -122.3321),
    "san francisco, us": (37.7749, -122.4194), "los angeles, us": (34.0522, -118.2437),
    "toronto, ca": (43.6532, -79.3832), "vancouver, ca": (49.2827, -123.1207), "montreal, ca": (45.5019, -73.5674),
    # APAC
    "singapore, sg": (1.3521, 103.8198), "sydney, au": (-33.8688, 151.2093), "melbourne, au": (-37.8136, 144.9631),
    "tokyo, jp": (35.6762, 139.6503), "seoul, kr": (37.5665, 126.9780), "hong kong, hk": (22.3193, 114.1694),
    "taipei, tw": (25.0330, 121.5654), "bangkok, th": (13.7563, 100.5018), "jakarta, id": (-6.2088, 106.8456),
    "bengaluru, in": (12.9716, 77.5946), "auckland, nz": (-36.8485, 174.7633),
    # LATAM
    "sao paulo, br": (-23.5505, -46.6333), "mexico city, mx": (19.4326, -99.1332), "buenos aires, ar": (-34.6037, -58.3816),
    "santiago, cl": (-33.4489, -70.6693), "bogota, co": (4.7110, -74.0721), "lima, pe": (-12.0464, -77.0428),
    # MEA
    "dubai, ae": (25.2048, 55.2708), "riyadh, sa": (24.7136, 46.6753), "cairo, eg": (30.0444, 31.2357),
    "casablanca, ma": (33.5731, -7.5898), "johannesburg, za": (-26.2041, 28.0473), "nairobi, ke": (-1.2921, 36.8219),
}

COUNTRY_ISO = {
    "france":"FR","germany":"DE","netherlands":"NL","belgium":"BE","luxembourg":"LU","switzerland":"CH","austria":"AT",
    "spain":"ES","portugal":"PT","italy":"IT","czech republic":"CZ","poland":"PL","hungary":"HU","denmark":"DK",
    "norway":"NO","sweden":"SE","finland":"FI","ireland":"IE","united kingdom":"GB","uk":"GB","england":"GB","scotland":"GB",
    "united states":"US","usa":"US","canada":"CA","mexico":"MX",
    "brazil":"BR","argentina":"AR","chile":"CL","colombia":"CO","peru":"PE",
    "singapore":"SG","australia":"AU","new zealand":"NZ","japan":"JP","south korea":"KR","hong kong":"HK","taiwan":"TW",
    "thailand":"TH","indonesia":"ID","philippines":"PH","india":"IN","vietnam":"VN","china":"CN",
    "united arab emirates":"AE","saudi arabia":"SA","qatar":"QA","bahrain":"BH","kuwait":"KW","oman":"OM",
    "israel":"IL","turkey":"TR","egypt":"EG","morocco":"MA","tunisia":"TN","south africa":"ZA","kenya":"KE","nigeria":"NG",
}

def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip().lower())

def _guess_country_iso_from_text(txt: str) -> Optional[str]:
    t = _norm(txt)
    for name, iso in COUNTRY_ISO.items():
        if name in t:
            return iso
    return None

def enrich_location(location: str):
    """
    Returns (city, country_iso2, lat, lon, region)
    """
    if not location:
        return None, None, None, None, None

    parts = [p.strip() for p in re.split(r"[,/|-]", location) if p.strip()]
    city_guess = parts[0] if parts else location

    iso = _guess_country_iso_from_text(location)
    if iso:
        key = f"{_norm(city_guess)}, {iso.lower()}"
        if key in CITY_DB:
            lat, lon = CITY_DB[key]
            return city_guess.strip().title(), iso, lat, lon, COUNTRY_REGION.get(iso)

    loc = _norm(location)
    for name, (lat, lon) in CITY_DB.items():
        ncity, cc = name.split(", ")
        if ncity in loc:
            iso2 = cc.upper()
            return ncity.title(), iso2, lat, lon, COUNTRY_REGION.get(iso2)

    if iso:
        return city_guess.strip(), iso, None, None, COUNTRY_REGION.get(iso)

    return city_guess.strip(), None, None, None, None
