from django import forms
from . import models


class TagForm(forms.ModelForm):
    class Meta:
        model = models.Tag
        fields = [
<<<<<<< HEAD
            # "created_at",
=======
            # "timestamp",
>>>>>>> 609159725a8427956399f25bc6c3d39cc33898e1
            "slug",
            "name",
        ]


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = [
            "published_at",
            "description",
            "is_public",
            "title",
            # "updated_at",
            "content",
            # "created_at",
            "category",
            "tags",
        ]


class FileForm(forms.ModelForm):
    class Meta:
        model = models.File
        fields = [
            "title",
            "file",
            # "binary",
            "post",
        ]


class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = [
            # "binary",
            "title",
            "image",
            "post",
        ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = [
<<<<<<< HEAD
            # "created_at",
=======
            # "timestamp",
>>>>>>> 609159725a8427956399f25bc6c3d39cc33898e1
            "name",
            "slug",
        ]
