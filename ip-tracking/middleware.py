from ipgeolocation import IpGeolocationAPI
from django.core.cache import cache

geo_api = IpGeolocationAPI("YOUR_API_KEY")

def get_geo(ip):
    cached = cache.get(f"geo:{ip}")
    if cached:
        return cached

    try:
        data = geo_api.get_geolocation_data(ip)
        result = {
            'country': data.get('country_name'),
            'city': data.get('city'),
        }
        cache.set(f"geo:{ip}", result, timeout=86400)
        return result
    except Exception:
        return {'country': None, 'city': None}
