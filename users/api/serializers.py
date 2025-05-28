from rest_framework import serializers
from users import models
from rest_framework.permissions import IsAuthenticated

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        permission_classes = [IsAuthenticated]
        model = models.User
        fields = '__all__'