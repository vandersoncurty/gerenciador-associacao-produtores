from django.db import models

# Create your models here.

class Slip(models.Model):
    member_id = models.ForeignKey('member.Member', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateTimeField()
    status = models.ForeignKey('slip_status.SlipStatus', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)