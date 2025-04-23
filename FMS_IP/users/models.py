from django.db import models
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm


class User(models.Model):
    username = models.CharField('Логин')
    email = models.EmailField('Почта')
    password1 = models.CharField('Пароль')
    password2 = models.CharField('Повтор пароля')
    #sf_trails = orm.relationship(Trail, back_populates='user')

    def __str__(self):
        return self.name



'''    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)'''
