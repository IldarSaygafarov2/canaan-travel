# Generated by Django 5.0.4 on 2024-04-12 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_tour_full_description_2_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='map_link',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка для карты'),
        ),
    ]