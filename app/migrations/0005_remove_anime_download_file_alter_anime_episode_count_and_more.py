# Generated by Django 5.1.1 on 2024-10-29 09:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_anime_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='download_file',
        ),
        migrations.AlterField(
            model_name='anime',
            name='episode_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Qismlar soni'),
        ),
        migrations.AlterField(
            model_name='anime',
            name='release_date',
            field=models.DateField(verbose_name='Chiqarilgan sana'),
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Epizod nomi')),
                ('video_file', models.FileField(upload_to='anime/videos/', verbose_name='Video fayl')),
                ('episode_number', models.PositiveIntegerField(verbose_name='Epizod raqami')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='app.anime', verbose_name='Anime')),
            ],
            options={
                'verbose_name': 'Epizod',
                'verbose_name_plural': 'Epizodlar',
                'ordering': ['episode_number'],
            },
        ),
    ]
