# Generated by Django 5.0.4 on 2024-04-13 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_hotelitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelitem',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='hotelitem',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
    ]
