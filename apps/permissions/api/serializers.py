from rest_framework import serializers
from apps.permissions import models

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Permission
        fields = '__all__'