from celery import shared_task
from django.utils.timezone import now, timedelta
from .models import RequestLog, SuspiciousIP

@shared_task
def detect_suspicious_ips():
    one_hour_ago = now() - timedelta(hours=1)
    logs = RequestLog.objects.filter(timestamp__gte=one_hour_ago)

    # Check for request count > 100
    from django.db.models import Count
    high_freq_ips = logs.values('ip_address').annotate(cnt=Count('id')).filter(cnt__gt=100)

    for entry in high_freq_ips:
        SuspiciousIP.objects.get_or_create(ip_address=entry['ip_address'], defaults={
            'reason': 'More than 100 requests in 1 hour'
        })

    # Check for access to sensitive paths
    for log in logs:
        if log.path in ['/admin', '/login']:
            SuspiciousIP.objects.get_or_create(ip_address=log.ip_address, defaults={
                'reason': f'Accessed sensitive path: {log.path}'
            })
