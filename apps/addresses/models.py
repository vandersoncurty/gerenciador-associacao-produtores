from django.db import models

# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=255)
    neightborhood = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.street}, {self.neightborhood}, {self.city}, {self.state}, {self.zip_code}, {self.country}"