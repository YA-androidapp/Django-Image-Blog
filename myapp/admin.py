from django.contrib import admin
from django import forms

from . import models


class TagAdminForm(forms.ModelForm):

    class Meta:
        model = models.Tag
        fields = "__all__"


class TagAdmin(admin.ModelAdmin):
    form = TagAdminForm
    list_display = [
        "name",
        "slug",
        "timestamp",
    ]
    readonly_fields = [
        "timestamp",
        # "slug",
        # "name",
    ]


class PostAdminForm(forms.ModelForm):

    class Meta:
        model = models.Post
        fields = "__all__"


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = [
        "title",
        "description",
        "content",
        "created_at",
        "updated_at",
        "published_at",
        "is_public",
    ]
    readonly_fields = [
        # "published_at",
        # "description",
        # "is_public",
        # "title",
        "updated_at",
        # "content",
        "created_at",
    ]


class FileAdminForm(forms.ModelForm):

    class Meta:
        model = models.File
        fields = "__all__"


class FileAdmin(admin.ModelAdmin):
    form = FileAdminForm
    list_display = [
        "title",
        "file",
        "binary",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "title",
        "file",
        # "created",
        # "last_updated",
        "binary",
    ]


class ImageAdminForm(forms.ModelForm):

    class Meta:
        model = models.Image
        fields = "__all__"


class ImageAdmin(admin.ModelAdmin):
    form = ImageAdminForm
    list_display = [
        "title",
        "image",
        "binary",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        # "last_updated",
        "binary",
        # "created",
        "title",
        "image",
    ]


class CategoryAdminForm(forms.ModelForm):

    class Meta:
        model = models.Category
        fields = "__all__"


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = [
        "name",
        "slug",
        "timestamp",
    ]
    readonly_fields = [
        # "timestamp",
        "name",
        "slug",
    ]


admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.File, FileAdmin)
admin.site.register(models.Image, ImageAdmin)
admin.site.register(models.Category, CategoryAdmin)
