# ip_tracking/models.py
from django.db import models

class RequestLog(models.Model):
    ip_address = models.CharField(max_length=45)  # Supports both IPv4 and IPv6
    timestamp = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ip_address} - {self.path}"