from django.shortcuts import render

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
