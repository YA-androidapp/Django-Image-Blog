from rest_framework import serializers

from . import models


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tag
        fields = [
<<<<<<< HEAD
            "created_at",
=======
            "timestamp",
>>>>>>> 609159725a8427956399f25bc6c3d39cc33898e1
            "slug",
            "name",
        ]

<<<<<<< HEAD

=======
>>>>>>> 609159725a8427956399f25bc6c3d39cc33898e1
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

<<<<<<< HEAD

=======
>>>>>>> 609159725a8427956399f25bc6c3d39cc33898e1
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

<<<<<<< HEAD

=======
>>>>>>> 609159725a8427956399f25bc6c3d39cc33898e1
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

<<<<<<< HEAD

=======
>>>>>>> 609159725a8427956399f25bc6c3d39cc33898e1
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = [
<<<<<<< HEAD
            "created_at",
=======
            "timestamp",
>>>>>>> 609159725a8427956399f25bc6c3d39cc33898e1
            "name",
            "slug",
        ]
