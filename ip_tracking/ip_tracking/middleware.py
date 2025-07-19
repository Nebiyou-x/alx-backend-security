# ip_tracking/middleware.py
import requests
from django.core.cache import cache
from ipware import get_client_ip

class IPLoggingMiddleware:
    # ... previous code ...

    def get_geolocation(self, ip):
        if not ip or ip == '127.0.0.1':
            return None, None
        
        cache_key = f'geo_{ip}'
        cached = cache.get(cache_key)
        if cached:
            return cached.get('country'), cached.get('city')
        
        try:
            response = requests.get(f'http://ip-api.com/json/{ip}?fields=country,city')
            data = response.json()
            country = data.get('country')
            city = data.get('city')
            
            # Cache for 24 hours (86400 seconds)
            cache.set(cache_key, {'country': country, 'city': city}, 86400)
            return country, city
        except:
            return None, None

    def __call__(self, request):
        ip, _ = get_client_ip(request)
        
        if not ip:
            ip = request.META.get('REMOTE_ADDR', '')
        
        country, city = self.get_geolocation(ip)
        
        RequestLog.objects.create(
            ip_address=ip,
            path=request.path,
            country=country,
            city=city
        )
        
        # Rest of the middleware...