from rest_framework import serializers
from apps.slip import models

class SlipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Slip
        fields = '__all__'