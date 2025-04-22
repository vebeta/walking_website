"""from django.db import models
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm


class User(models.Model):
    name = models.CharField('Имя', max_length=40)
    surname = models.TextField('Фамилия', max_length=40)
    birth_date = models.DateField('Дата рождения')
    email = models.EmailField('Электронная почта', unique=True)
    hashed_password = models.CharField('Пароль')
    #sf_trails = orm.relationship(Trail, back_populates='user')

    def __str__(self):
        return self.name



'''    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)'''
"""