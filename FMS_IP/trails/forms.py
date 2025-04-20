from django import forms
from .models import *


class AddTrailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.fields['categ'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Trail
        fields = ['title', 'description', 'categ']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'descr': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }