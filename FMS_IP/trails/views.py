from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .models import *
from .forms import *
from .utils import *


class TrailsHome(DataMixin, ListView):
    model = Trail
    template_name = 'trails/trails.html'
    context_object_name = 'obj'
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        uniq_ctxt = self.get_user_context(title='Маршруты')
        return dict(list(context.items()) + list(uniq_ctxt.items()))

    def get_queryset(self):
        return Trail.objects.filter(is_published=True)


class TrailPage(DataMixin, DetailView):
    model = Trail
    template_name = 'trails/trail_page.html'
    slug_url_kwarg = 'trl_slug'
    context_object_name = 'trail'


class AddTrail(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddTrailForm
    template_name = 'trails/add_trail.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        uniq_ctxt = self.get_user_context(title='Добавление маршрута')
        return dict(list(context.items()) + list(uniq_ctxt.items()))
