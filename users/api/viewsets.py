from rest_framework import viewsets
from users.api import serializers
from users import models
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    permission_classes = [IsAuthenticated]