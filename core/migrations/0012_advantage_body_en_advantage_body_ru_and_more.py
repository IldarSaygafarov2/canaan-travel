# Generated by Django 5.0.4 on 2024-04-05 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='advantage',
            name='body_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='advantage',
            name='body_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='advantage',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='advantage',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='article',
            name='excerpt_en',
            field=models.TextField(max_length=500, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='article',
            name='excerpt_ru',
            field=models.TextField(max_length=500, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='article',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='article',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='destination',
            name='short_description_en',
            field=models.TextField(max_length=250, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='destination',
            name='short_description_ru',
            field=models.TextField(max_length=250, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='destination',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='destination',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='tour',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='tour',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
    ]