# Generated by Django 5.0.4 on 2024-04-11 17:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_tour_destination'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='short_descrtion',
            field=models.TextField(max_length=500, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='destination',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.destination', verbose_name='Направление'),
        ),
    ]
