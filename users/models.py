from django.db import models

# Create your models here.

class User(models.Model):
    """
    User model for the GAR application.
    """
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    role = models.CharField(max_length=50, choices=[
        ('admin', 'Admin'),
        ('partner', 'Partner'),
        ('associate', 'Associate'),
    ], default='associate', help_text="User role in the system")
