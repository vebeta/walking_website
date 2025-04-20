from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView
from .forms import RegisterUserForm

'''urls_lst = {
    'home': 'home',
    'about': 'about',
    'trails': 'trails',
    'register': 'register',
    'login': 'login',
    'profile': 'profile'
}
'''

def index(request):
    data = {
        'title': 'Главная'
    }
    return render(request, 'main_page/index.html', data)

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



def login(request):
    data = {
        'title': 'Войти'
    }
    return render(request, 'main_page/login_form.html', data)

def profile(request):
    data = {
        'title': 'Профиль',
        #'obj': User.objects.all()
    }
    return render(request, 'main_page/profile.html', data)