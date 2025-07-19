class BlockedIP(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
