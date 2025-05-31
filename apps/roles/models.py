from django.db import models

# Create your models here.

class Role(models.Model):

    """
    Role model for the GAR application.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    permission_id = models.ForeignKey(
        'permissions.Permission',
        on_delete=models.CASCADE,
        related_name='roles'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'