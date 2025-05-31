from rest_framework import viewsets
from apps.system_config.api import serializers
from apps.system_config import models
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter

@extend_schema(tags=['System Config'])
class SystemConfigViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SystemConfigSerializer
    queryset = models.SystemConfig.objects.all()
    permission_classes = [IsAuthenticated]