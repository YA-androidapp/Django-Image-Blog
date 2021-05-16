from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("UserGroup", api.UserGroupViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("users/UserGroup/", views.UserGroupListView.as_view(), name="users_UserGroup_list"),
    path("users/UserGroup/create/", views.UserGroupCreateView.as_view(), name="users_UserGroup_create"),
    path("users/UserGroup/detail/<int:pk>/", views.UserGroupDetailView.as_view(), name="users_UserGroup_detail"),
    path("users/UserGroup/update/<int:pk>/", views.UserGroupUpdateView.as_view(), name="users_UserGroup_update"),
)
