from django.db import models

class Trail(models.Model):
    title = models.CharField('Название', max_length=70)
    description = models.TextField('Описание')
    date = models.DateTimeField('Дата создания', auto_now=True)
    rate = models.IntegerField('Рейтинг', default=0)
    is_published = models.BooleanField(default=True)

    #user = orm.relationship('User')

    def __str__(self):
        return self.title