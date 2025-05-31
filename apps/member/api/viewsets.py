from rest_framework import viewsets
from apps.member.api import serializers
from apps.member import models
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter

@extend_schema(tags=['Members'])
class MemberViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MemberSerializer
    queryset = models.Member.objects.all()
    permission_classes = [IsAuthenticated]