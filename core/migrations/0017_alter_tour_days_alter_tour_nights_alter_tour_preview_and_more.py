# Generated by Django 5.0.4 on 2024-04-11 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_tour_days_alter_tour_nights_alter_tour_preview_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='days',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Дней'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='nights',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Ночей'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='tours/', verbose_name='Заставка'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='short_description',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Краткое описание'),
        ),
    ]