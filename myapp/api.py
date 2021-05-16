from rest_framework import viewsets, permissions

from . import serializers
from . import models


class TagViewSet(viewsets.ModelViewSet):
    """ViewSet for the Tag class"""

    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet for the Post class"""

    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class FileViewSet(viewsets.ModelViewSet):
    """ViewSet for the File class"""

    queryset = models.File.objects.all()
    serializer_class = serializers.FileSerializer
    permission_classes = [permissions.IsAuthenticated]


class ImageViewSet(viewsets.ModelViewSet):
    """ViewSet for the Image class"""

    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the Category class"""

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
