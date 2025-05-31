from django.db import models

# Create your models here.

class User(models.Model):
    """
    User model for the GAR application.
    """
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    role = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True)
