from rest_framework import viewsets
from addresses.api import serializers
from addresses import models
from rest_framework.permissions import IsAuthenticated

class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AddressSerializer
    queryset = models.Address.objects.all()
    permission_classes = [IsAuthenticated]