from rest_framework import viewsets
from contacts.api import serializers
from contacts import models
from rest_framework.permissions import IsAuthenticated

class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ContactSerializer
    queryset = models.Contact.objects.all()
    permission_classes = [IsAuthenticated]