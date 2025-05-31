from rest_framework import viewsets
from apps.users.api import serializers
from apps.users import models
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter

@extend_schema(tags=['Users'])
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    permission_classes = [IsAuthenticated]