# Generated by Django 5.0.4 on 2024-04-05 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_advantage'),
    ]

    operations = [
        migrations.AddField(
            model_name='advantage',
            name='icon',
            field=models.ImageField(null=True, upload_to='advantages', verbose_name='Иконка'),
        ),
    ]