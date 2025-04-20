from django.db import models

class Trail(models.Model):
    title = models.CharField('Название', max_length=70)
    description = models.TextField('Описание')
    date = models.DateTimeField('Дата создания', auto_now=True)
    rate = models.IntegerField('Рейтинг', default=0)
    is_published = models.BooleanField(default=True)

    categ = models.ManyToManyField('Category') # , on_delete=models.SET_NULL

    #user = orm.relationship('User')

    def __str__(self):
        return self.title

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