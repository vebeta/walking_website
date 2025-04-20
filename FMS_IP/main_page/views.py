from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

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