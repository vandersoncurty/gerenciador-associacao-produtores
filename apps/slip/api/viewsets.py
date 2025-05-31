from rest_framework import viewsets
from apps.slip.api import serializers
from apps.slip import models
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter

@extend_schema(tags=['Slips'])
class SlipViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SlipSerializer
    queryset = models.Slip.objects.all()
    permission_classes = [IsAuthenticated]