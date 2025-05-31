from django.db import models

# Create your models here.

class SystemInfo(models.Model):
    """
    Model to store system info.
    """
    key = models.CharField(max_length=255, unique=True, verbose_name="Info Key")
    value = models.TextField(verbose_name="Info Value")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    class Meta:
        verbose_name = "System Info"
        verbose_name_plural = "System Infos"

    def __str__(self):
        return f"{self.key}: {self.value}"