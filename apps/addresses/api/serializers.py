from rest_framework import serializers
from apps.addresses import models

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = '__all__'