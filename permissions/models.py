from django.db import models

# Create your models here.

class Permission(models.Model):
    """
    Permission model for the GAR application.
    """
    can_view_users = models.BooleanField(default=False)
    can_edit_users = models.BooleanField(default=False)
    can_delete_users = models.BooleanField(default=False)
    can_view_roles = models.BooleanField(default=False)
    can_edit_roles = models.BooleanField(default=False)
    can_delete_roles = models.BooleanField(default=False)
    can_view_permissions = models.BooleanField(default=False)
    can_edit_permissions = models.BooleanField(default=False)
    can_delete_permissions = models.BooleanField(default=False)
    can_view_members = models.BooleanField(default=False)
    can_edit_members = models.BooleanField(default=False)
    can_delete_members = models.BooleanField(default=False)
    can_view_slips = models.BooleanField(default=False)
    can_edit_slips = models.BooleanField(default=False)
    can_delete_slips = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
