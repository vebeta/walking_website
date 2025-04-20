from django import forms
from .models import *

class RegisterForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=40)
    surname = forms.CharField(label='Фамилия', max_length=40)
    birth_date = forms.DateField(label='Дата рождения')
    email = forms.EmailField(label='Почта', unique=True)
    hashed_password = forms.CharField(label='Пароль')

    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #c_def = self.get_user_context(title='Регистрация')
        #return (list(context.items()) + list(c_def.items()))


class LoginForm(forms.Form):
    email = forms.EmailField(label='Почта', unique=True)
    hashed_password = forms.CharField(label='Пароль')