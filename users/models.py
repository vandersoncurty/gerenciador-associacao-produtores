from django.db import models

# Create your models here.

class User(models.Model):
    """
    User model for the GAR application.
    """
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True, blank=True, null=True)
    rg = models.CharField(max_length=10, unique=True, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    profission = models.CharField(max_length=50, blank=True, null=True)
    spouse = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    role_id = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True, related_name='users')
    address_id = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True, related_name='users')
    contact_id = models.ForeignKey('Contact', on_delete=models.SET_NULL, null=True, related_name='users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
