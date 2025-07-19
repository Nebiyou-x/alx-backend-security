class SuspiciousIP(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    reason = models.TextField()
