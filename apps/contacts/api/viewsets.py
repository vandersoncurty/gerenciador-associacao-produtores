from rest_framework import viewsets
from apps.contacts.api import serializers
from apps.contacts import models
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter

@extend_schema(tags=['Contacts'])
class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ContactSerializer
    queryset = models.Contact.objects.all()
    permission_classes = [IsAuthenticated]