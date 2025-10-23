from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Trail(models.Model):
    title = models.CharField('Название', max_length=70)
    description = models.TextField('Описание')
    map = models.CharField('Карта', default='') # <script type="text/javascript" charset="utf-8" async src="{{ trail.map }}"></script>
    date = models.DateTimeField('Дата создания', auto_now=True)
    rate = models.IntegerField('Рейтинг', default=0)
    is_published = models.BooleanField(default=True)

    slug = models.SlugField('URL', unique=True, max_length=255, db_index=True)

    categ = models.ManyToManyField('Category') # , on_delete=models.SET_NULL
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='created_trails', null=True)

    #user = orm.relationship('User')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('trail', kwargs={'trl_slug': self.slug})

    class Meta:
        verbose_name = "Маршрут"
        verbose_name_plural = "Маршруты"
        ordering = ['date', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['id']