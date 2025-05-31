from rest_framework import viewsets
from apps.system_info.api import serializers
from apps.system_info import models
from drf_spectacular.utils import extend_schema, OpenApiParameter

@extend_schema(tags=['System Info'])
class SystemInfoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SystemInfoSerializer
    queryset = models.SystemInfo.objects.all()