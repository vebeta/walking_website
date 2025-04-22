from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView
from .forms import RegisterUserForm, LoginUserForm

'''urls_lst = {
    'home': 'home',
    'about': 'about',
    'trails': 'trails',
    'register': 'register',
    'login': 'login',
    'profile': 'profile'
}
'''

def home_page(request):
    data = {
        'title': 'Главная'
    }
    return render(request, 'main_page/home_page.html', data)

def about(request):
    data = {
        'title': 'О нас'
    }
    return render(request, 'main_page/about.html', data)

#def pageNotFound(request, exception):
#    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main_page/register_form.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main_page/login_form.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context


def profile(request):
    data = {
        'title': 'Профиль',
        #'obj': User.objects.all()
    }
    return render(request, 'main_page/profile.html', data)


def logout_user(request):
    logout(request)
    return redirect('home')