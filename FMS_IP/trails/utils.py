from .models import *


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        categs = Category.objects.all()
        context['categs'] = categs
        return context