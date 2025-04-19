from django.shortcuts import render
from .models import Trail

def trails(request):
    data = {
        'title': 'Маршруты',
        'obj': Trail.objects.all()
    }
    return render(request, 'trails/trails.html', data)
