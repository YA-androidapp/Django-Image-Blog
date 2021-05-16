from django.views import generic
from . import models
from . import forms


class UserGroupListView(generic.ListView):
    model = models.UserGroup
    form_class = forms.UserGroupForm


class UserGroupCreateView(generic.CreateView):
    model = models.UserGroup
    form_class = forms.UserGroupForm


class UserGroupDetailView(generic.DetailView):
    model = models.UserGroup
    form_class = forms.UserGroupForm


class UserGroupUpdateView(generic.UpdateView):
    model = models.UserGroup
    form_class = forms.UserGroupForm
    pk_url_kwarg = "pk"
