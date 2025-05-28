from django.db import models

# Create your models here.

class User(models.Model):
    """
    User model for the GAR application.
    """
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=50, choices=[
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('user', 'User'),
    ], default='user', help_text="User role in the system")
