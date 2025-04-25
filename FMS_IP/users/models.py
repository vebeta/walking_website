from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    first_name = models.CharField('', blank=True, null=True, default='')
    birth_date = models.DateTimeField('Дата рождения', blank=True, null=True)
    slug = models.SlugField('URL', unique=True, max_length=255, db_index=True)
    #sf_trails = orm.relationship(Trail, back_populates='user')

    #def show(self):
        #return list(self.username, self.first_name, self.last_name, self.email, self.birth_date)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'usr_slug': self.slug})