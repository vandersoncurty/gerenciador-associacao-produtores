from rest_framework import viewsets
from apps.addresses.api import serializers
from apps.addresses import models
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter

@extend_schema(tags=['Addresses'])
class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AddressSerializer
    queryset = models.Address.objects.all()
    permission_classes = [IsAuthenticated]