from django.db import models

from reports import empty_template


class Report(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    template = models.TextField(verbose_name='Шаблон', default=empty_template.text)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'
