from rest_framework import viewsets
from apps.permissions.api import serializers
from apps.permissions import models
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter

@extend_schema(tags=['Permissions'])
class PermissionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PermissionSerializer
    queryset = models.Permission.objects.all()
    permission_classes = [IsAuthenticated]