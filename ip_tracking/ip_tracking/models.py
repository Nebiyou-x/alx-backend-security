# ip_tracking/models.py
class SuspiciousIP(models.Model):
    ip_address = models.CharField(max_length=45)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - {self.reason[:50]}"