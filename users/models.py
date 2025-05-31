from django.db import models
from contacts.models import Contact
from addresses.models import Address
from roles.models import Role
from permissions.models import Permission

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
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, related_name='users')
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, related_name='users')
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True, related_name='users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
