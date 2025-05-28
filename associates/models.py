from django.db import models

# Create your models here.

class Associate(models.Model):
    """
    Associate model for the GAR application.
    """
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
