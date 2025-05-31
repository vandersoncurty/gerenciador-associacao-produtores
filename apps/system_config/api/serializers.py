from rest_framework import serializers
from apps.system_config import models

class SystemConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SystemConfig
        fields = '__all__'