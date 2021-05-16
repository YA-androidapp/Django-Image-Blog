from rest_framework import serializers

from . import models


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tag
        fields = [
            "created_at",
            "slug",
            "name",
        ]


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        fields = [
            "published_at",
            "description",
            "is_public",
            "title",
            "updated_at",
            "content",
            "created_at",
        ]


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.File
        fields = [
            "title",
            "file",
            "created",
            "last_updated",
            "binary",
        ]


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = [
            "last_updated",
            "binary",
            "created",
            "title",
            "image",
        ]


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = [
            "created_at",
            "name",
            "slug",
        ]
