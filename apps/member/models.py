from django.db import models

# Create your models here.

class Member(models.Model):
    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    car_plate = models.CharField(max_length=10, blank=True, null=True)
    car_model = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('banned', 'Banned'),
    ])
    pay_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_id}"

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"
        ordering = ['date_joined']  # Order by date joined by default