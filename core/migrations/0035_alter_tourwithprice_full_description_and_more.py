# Generated by Django 5.0.4 on 2024-04-16 23:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_alter_tourcondition_options_alter_tourhotel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourwithprice',
            name='full_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Детали'),
        ),
        migrations.AlterField(
            model_name='tourwithprice',
            name='full_description_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Детали'),
        ),
        migrations.AlterField(
            model_name='tourwithprice',
            name='full_description_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Детали'),
        ),
    ]