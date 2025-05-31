from rest_framework import viewsets
from apps.slip_status.api import serializers
from apps.slip_status import models
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter

@extend_schema(tags=['Slip Status'])
class SlipStatusViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SlipStatusSerializer
    queryset = models.SlipStatus.objects.all()
    permission_classes = [IsAuthenticated]