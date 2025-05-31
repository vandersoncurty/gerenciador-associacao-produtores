from rest_framework import viewsets
from permissions.api import serializers
from permissions import models
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter

@extend_schema(tags=['Permissions'])
class PermissionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PermissionSerializer
    queryset = models.Permission.objects.all()
    permission_classes = [IsAuthenticated]