from rest_framework import serializers
from apps.member import models

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Member
        fields = '__all__'