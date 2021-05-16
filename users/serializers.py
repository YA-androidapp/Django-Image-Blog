from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = [
            "uuid",
            "name",
            "username",
            "is_staff",
            "date_joined",
            "first_name",
            "last_name",
            "email",
        ]

class UserGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserGroup
        fields = [
            "name",
        ]
