# ip_tracking/models.py
class RequestLog(models.Model):
    # Previous fields...
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)