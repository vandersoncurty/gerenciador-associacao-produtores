from rest_framework import viewsets
from roles.api import serializers
from roles import models
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter

@extend_schema(tags=['Roles'])
class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RoleSerializer
    queryset = models.Role.objects.all()
    permission_classes = [IsAuthenticated]