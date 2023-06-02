from django.db import models
from organizations.models import Organizations


class Events(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    organizations = models.ManyToManyField(Organizations)
    image = models.ImageField('Превью')
    date = models.DateTimeField('Время и дата')

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.title


