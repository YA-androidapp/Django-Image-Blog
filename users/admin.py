from . import models
from .models import User, UserGroup
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _


@admin.register(UserGroup)
class AdminUserGroup(admin.ModelAdmin):
    pass


@admin.register(User)
class AdminUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('last_name', 'first_name', 'email','departments')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'last_name', 'first_name', 'is_staff')
    search_fields = ('username', 'last_name', 'first_name', 'email')
    filter_horizontal = ('groups', 'user_permissions','departments')


class UserGroupAdminForm(forms.ModelForm):
    class Meta:
        model = models.UserGroup
        fields = "__all__"


class UserGroupAdmin(admin.ModelAdmin):
    form = UserGroupAdminForm
    list_display = [
        "name",
    ]
    readonly_fields = [
        # "name",
    ]
