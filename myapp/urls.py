from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Tag", api.TagViewSet)
router.register("Post", api.PostViewSet)
router.register("File", api.FileViewSet)
router.register("Image", api.ImageViewSet)
router.register("Category", api.CategoryViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
<<<<<<< HEAD
    path("myapp/Category/", views.CategoryListView.as_view(), name="myapp_Category_list"),
    path("myapp/Category/create/", views.CategoryCreateView.as_view(), name="myapp_Category_create"),
    path("myapp/Category/detail/<slug:slug>/", views.CategoryDetailView.as_view(), name="myapp_Category_detail"),
    path("myapp/Category/update/<slug:slug>/", views.CategoryUpdateView.as_view(), name="myapp_Category_update"),
=======
    path("myapp/Tag/", views.TagListView.as_view(), name="myapp_Tag_list"),
    path("myapp/Tag/create/", views.TagCreateView.as_view(), name="myapp_Tag_create"),
    path("myapp/Tag/detail/<slug:slug>/", views.TagDetailView.as_view(), name="myapp_Tag_detail"),
    path("myapp/Tag/update/<slug:slug>/", views.TagUpdateView.as_view(), name="myapp_Tag_update"),
    path("myapp/Post/", views.PostListView.as_view(), name="myapp_Post_list"),
    path("myapp/Post/create/", views.PostCreateView.as_view(), name="myapp_Post_create"),
    path("myapp/Post/detail/<int:pk>/", views.PostDetailView.as_view(), name="myapp_Post_detail"),
    path("myapp/Post/update/<int:pk>/", views.PostUpdateView.as_view(), name="myapp_Post_update"),
>>>>>>> 609159725a8427956399f25bc6c3d39cc33898e1
    path("myapp/File/", views.FileListView.as_view(), name="myapp_File_list"),
    path("myapp/File/create/", views.FileCreateView.as_view(), name="myapp_File_create"),
    path("myapp/File/detail/<int:pk>/", views.FileDetailView.as_view(), name="myapp_File_detail"),
    path("myapp/File/update/<int:pk>/", views.FileUpdateView.as_view(), name="myapp_File_update"),
    path("myapp/Image/", views.ImageListView.as_view(), name="myapp_Image_list"),
    path("myapp/Image/create/", views.ImageCreateView.as_view(), name="myapp_Image_create"),
    path("myapp/Image/detail/<int:pk>/", views.ImageDetailView.as_view(), name="myapp_Image_detail"),
    path("myapp/Image/update/<int:pk>/", views.ImageUpdateView.as_view(), name="myapp_Image_update"),
<<<<<<< HEAD
    path("myapp/Post/", views.PostListView.as_view(), name="myapp_Post_list"),
    path("myapp/Post/create/", views.PostCreateView.as_view(), name="myapp_Post_create"),
    path("myapp/Post/detail/<int:pk>/", views.PostDetailView.as_view(), name="myapp_Post_detail"),
    path("myapp/Post/update/<int:pk>/", views.PostUpdateView.as_view(), name="myapp_Post_update"),
    path("myapp/Tag/", views.TagListView.as_view(), name="myapp_Tag_list"),
    path("myapp/Tag/create/", views.TagCreateView.as_view(), name="myapp_Tag_create"),
    path("myapp/Tag/detail/<slug:slug>/", views.TagDetailView.as_view(), name="myapp_Tag_detail"),
    path("myapp/Tag/update/<slug:slug>/", views.TagUpdateView.as_view(), name="myapp_Tag_update"),
=======
    path("myapp/Category/", views.CategoryListView.as_view(), name="myapp_Category_list"),
    path("myapp/Category/create/", views.CategoryCreateView.as_view(), name="myapp_Category_create"),
    path("myapp/Category/detail/<slug:slug>/", views.CategoryDetailView.as_view(), name="myapp_Category_detail"),
    path("myapp/Category/update/<slug:slug>/", views.CategoryUpdateView.as_view(), name="myapp_Category_update"),
>>>>>>> 609159725a8427956399f25bc6c3d39cc33898e1
)
