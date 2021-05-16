from django import forms
from . import models


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = [
            "username",
            "last_name",
            "first_name",
            "email",
            "departments",
            "is_staff",
        ]


class UserGroupForm(forms.ModelForm):
    class Meta:
        model = models.UserGroup
        fields = [
            "name",
        ]
