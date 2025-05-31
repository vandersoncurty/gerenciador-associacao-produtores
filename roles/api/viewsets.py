from rest_framework import viewsets
from permissions.api import serializers
from roles import models
from rest_framework.permissions import IsAuthenticated

class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RoleSerializer
    queryset = models.Role.objects.all()
    permission_classes = [IsAuthenticated]