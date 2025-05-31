from rest_framework import serializers
from apps.slip_status import models

class SlipStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SlipStatus
        fields = '__all__'