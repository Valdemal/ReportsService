# Generated by Django 4.2.6 on 2023-11-03 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('template', models.TextField(default='<!DOCTYPE document SYSTEM "rml.dtd">\n<document filename="my_story.pdf">\n <template>\n     <!-- Данная секция содержит элементы документа с фиксированной позицией -->\n     <pageTemplate id="main">\n        <frame id="first" x1="100" y1="400" width="300" height="400"/>\n     </pageTemplate>\n </template>\n <stylesheet>\n     <!-- Данная секция содержит информацию о стилях -->\n     <paraStyle name="header" fontSize="16" fontName="Arial" leading="16"/>\n </stylesheet>\n <story>\n    <!-- Этот раздел содержит плавающие элементы документа. Эти элементы будут заполнять фреймы, определенные в -->\n    <!-- разделе <template> выше -->\n\n    <para style="header">\n        <b>Мой первый отчет в RML</b>\n    </para>\n    <para></para>\n </story>\n</document>', verbose_name='Шаблон')),
            ],
            options={
                'verbose_name': 'Отчет',
                'verbose_name_plural': 'Отчеты',
            },
        ),
    ]
