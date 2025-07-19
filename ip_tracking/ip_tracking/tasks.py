# ip_tracking/tasks.py
from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import RequestLog, SuspiciousIP

@shared_task
def detect_suspicious_ips():
    one_hour_ago = timezone.now() - timedelta(hours=1)
    sensitive_paths = ['/admin/', '/login/', '/wp-admin/']
    
    # Detect high request volumes
    from django.db.models import Count
    suspicious_ips = (
        RequestLog.objects
        .filter(timestamp__gte=one_hour_ago)
        .values('ip_address')
        .annotate(count=Count('ip_address'))
        .filter(count__gt=100)
    )
    
    for entry in suspicious_ips:
        SuspiciousIP.objects.create(
            ip_address=entry['ip_address'],
            reason=f"High request volume: {entry['count']} in last hour"
        )
    
    # Detect access to sensitive paths
    for path in sensitive_paths:
        sensitive_access = (
            RequestLog.objects
            .filter(timestamp__gte=one_hour_ago, path__startswith=path)
            .values('ip_address')
            .distinct()
        )
        
        for entry in sensitive_access:
            SuspiciousIP.objects.create(
                ip_address=entry['ip_address'],
                reason=f"Access to sensitive path: {path}"
            )