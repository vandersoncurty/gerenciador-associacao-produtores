from rest_framework import serializers
from apps.system_info import models

class SystemInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SystemInfo
        fields = '__all__'