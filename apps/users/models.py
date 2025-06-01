from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from apps.contacts.models import Contact
from apps.addresses.models import Address

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    """
    User model for the GAR application.
    """
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True, blank=True, null=True)
    rg = models.CharField(max_length=10, unique=True, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    profession = models.CharField(max_length=50, blank=True, null=True)
    spouse = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, related_name='users')
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True, related_name='users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []