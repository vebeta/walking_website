from django.contrib.auth import logout, login, get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView, DetailView
from .forms import RegisterUserForm, LoginUserForm
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register_form.html'
    success_url = reverse_lazy('users:login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('users:profile')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login_form.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('users:profile')


class ProfileUser(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'users/profile.html'
    slug_url_kwarg = 'usr_slug'
    context_object_name = 'usr_obj'

    '''def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        context['obj'] = self.request.user.objects.all()
        return context

    def get_object(self, queryset=None):
        return  self.request.user'''


'''def profile(request):
    data = {
        'title': 'Профиль',
        #'obj': User.objects.all()
    }
    return render(request, 'users/profile.html', data)'''


def logout_user(request):
    logout(request)
    return redirect('home')


def password_reset(request):
    return redirect('users:login')