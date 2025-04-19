from django.shortcuts import render
from .models import User

def register(request):
    data = {
        'title': 'Зарегистрироваться'
    }
    return render(request, 'users/register_form.html', data)

def login(request):
    data = {
        'title': 'Войти'
    }
    return render(request, 'users/login_form.html', data)

def profile(request):
    data = {
        'title': 'Профиль',
        'obj': User.objects.all()
    }
    return render(request, 'users/profile.html', data)