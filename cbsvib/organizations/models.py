from django.db import models


class Organizations(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    address = models.CharField('Адрес', max_length=1024)
    postcode = models.CharField('Почтовый индекс', max_length=6)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return self.title
