from django.db import models

# Create your models here.

class SystemConfig(models.Model):
    """
    Model to store system configuration settings.
    """
    key = models.CharField(max_length=255, unique=True, verbose_name="Configuration Key")
    value = models.TextField(verbose_name="Configuration Value")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    class Meta:
        verbose_name = "System Configuration"
        verbose_name_plural = "System Configurations"

    def __str__(self):
        return f"{self.key}: {self.value}"