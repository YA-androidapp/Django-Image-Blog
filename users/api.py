from rest_framework import viewsets, permissions

from . import serializers
from . import models


class UserGroupViewSet(viewsets.ModelViewSet):
    """ViewSet for the UserGroup class"""

    queryset = models.UserGroup.objects.all()
    serializer_class = serializers.UserGroupSerializer
    permission_classes = [permissions.IsAuthenticated]
