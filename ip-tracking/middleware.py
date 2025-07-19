from django.http import HttpResponseForbidden
from .models import BlockedIP, RequestLog

class RequestLoggingMiddleware:
    ...
    def __call__(self, request):
        ip = self.get_ip(request)

        # Block IP if blacklisted
        if BlockedIP.objects.filter(ip_address=ip).exists():
            return HttpResponseForbidden("Access denied")

        # Log the request
        RequestLog.objects.create(ip_address=ip, path=request.path)
        return self.get_response(request)
