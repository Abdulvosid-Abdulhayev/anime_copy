# Generated by Django 5.1.1 on 2024-10-29 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_anime_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='slug',
            field=models.SlugField(default='', max_length=255, verbose_name='Slug'),
        ),
    ]