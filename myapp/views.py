<<<<<<< HEAD
from . import forms
from . import models
from django.views import generic
=======
from django.views import generic
from . import models
from . import forms
>>>>>>> 609159725a8427956399f25bc6c3d39cc33898e1


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

<<<<<<< HEAD
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'categories': models.Category.objects.all(),
            'images': models.Image.objects.all(),
            'tags': models.Tag.objects.all(),
        })
        return context

=======
>>>>>>> 609159725a8427956399f25bc6c3d39cc33898e1

class PostDetailView(generic.DetailView):
    model = models.Post
    form_class = forms.PostForm


class PostUpdateView(generic.UpdateView):
    model = models.Post
    form_class = forms.PostForm
    pk_url_kwarg = "pk"

<<<<<<< HEAD
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'categories': models.Category.objects.all(),
            'images': models.Image.objects.all(),
            'tags': models.Tag.objects.all(),
        })
        return context

=======
>>>>>>> 609159725a8427956399f25bc6c3d39cc33898e1

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

<<<<<<< HEAD
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'posts': models.Post.objects.all(),
        })
        return context

=======
>>>>>>> 609159725a8427956399f25bc6c3d39cc33898e1

class ImageDetailView(generic.DetailView):
    model = models.Image
    form_class = forms.ImageForm


class ImageUpdateView(generic.UpdateView):
    model = models.Image
    form_class = forms.ImageForm
    pk_url_kwarg = "pk"

<<<<<<< HEAD
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'posts': models.Post.objects.all(),
        })
        return context

=======
>>>>>>> 609159725a8427956399f25bc6c3d39cc33898e1

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
