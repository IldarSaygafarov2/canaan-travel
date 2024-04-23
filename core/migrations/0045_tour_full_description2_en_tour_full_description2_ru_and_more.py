# Generated by Django 5.0.4 on 2024-04-22 21:45

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_tour_full_description2'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='full_description2_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Полное описание 2'),
        ),
        migrations.AddField(
            model_name='tour',
            name='full_description2_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Полное описание 2'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='full_description2',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Полное описание 2'),
        ),
    ]