# Generated by Django 5.0.4 on 2024-04-13 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_remove_tour_full_description_2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('name_ru', models.CharField(max_length=100, null=True, verbose_name='Название')),
                ('name_en', models.CharField(max_length=100, null=True, verbose_name='Название')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('slug', models.SlugField(verbose_name='Слаг')),
                ('preview', models.ImageField(upload_to='hotels/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Отель',
                'verbose_name_plural': 'Отели',
            },
        ),
    ]
