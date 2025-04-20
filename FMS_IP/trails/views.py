from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .models import *
from .forms import *


class TrailsHome(ListView):
    model = Trail
    template_name = 'trails/trails.html'
    context_object_name = 'obj'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Маршруты'
        return context

    def get_queryset(self):
        return Trail.objects.filter(is_published=True)


def trail_page(request, trl_id):
    trail = get_object_or_404(Trail, pk=trl_id)
    data = {
        'title': trail.title,
        'trail': trail
    }
    return render(request, 'trails/trail.html', data)

def add_trail(request):
    if request.method == 'POST':
        print('ok')
        form = AddTrailForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('trails')
            except:
                form.add_error(None, 'Ошибка добавления маршрута')
    else:
        print('bl')
        form = AddTrailForm()
    return render(request, 'trails/add_trail.html', {'title': 'Добавление маршрута', 'form': form})