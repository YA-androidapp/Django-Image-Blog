from django.views import generic
from . import models
from . import forms


class TagListView(generic.ListView):
    model = models.Tag
    form_class = forms.TagForm


class TagCreateView(generic.CreateView):
    model = models.Tag
    form_class = forms.TagForm


class TagDetailView(generic.DetailView):
    model = models.Tag
    form_class = forms.TagForm
    slug_url_kwarg = "slug"


class TagUpdateView(generic.UpdateView):
    model = models.Tag
    form_class = forms.TagForm
    slug_url_kwarg = "slug"


class PostListView(generic.ListView):
    model = models.Post
    form_class = forms.PostForm


class PostCreateView(generic.CreateView):
    model = models.Post
    form_class = forms.PostForm


class PostDetailView(generic.DetailView):
    model = models.Post
    form_class = forms.PostForm


class PostUpdateView(generic.UpdateView):
    model = models.Post
    form_class = forms.PostForm
    pk_url_kwarg = "pk"


class FileListView(generic.ListView):
    model = models.File
    form_class = forms.FileForm


class FileCreateView(generic.CreateView):
    model = models.File
    form_class = forms.FileForm


class FileDetailView(generic.DetailView):
    model = models.File
    form_class = forms.FileForm


class FileUpdateView(generic.UpdateView):
    model = models.File
    form_class = forms.FileForm
    pk_url_kwarg = "pk"


class ImageListView(generic.ListView):
    model = models.Image
    form_class = forms.ImageForm


class ImageCreateView(generic.CreateView):
    model = models.Image
    form_class = forms.ImageForm


class ImageDetailView(generic.DetailView):
    model = models.Image
    form_class = forms.ImageForm


class ImageUpdateView(generic.UpdateView):
    model = models.Image
    form_class = forms.ImageForm
    pk_url_kwarg = "pk"


class CategoryListView(generic.ListView):
    model = models.Category
    form_class = forms.CategoryForm


class CategoryCreateView(generic.CreateView):
    model = models.Category
    form_class = forms.CategoryForm


class CategoryDetailView(generic.DetailView):
    model = models.Category
    form_class = forms.CategoryForm
    slug_url_kwarg = "slug"


class CategoryUpdateView(generic.UpdateView):
    model = models.Category
    form_class = forms.CategoryForm
    slug_url_kwarg = "slug"
