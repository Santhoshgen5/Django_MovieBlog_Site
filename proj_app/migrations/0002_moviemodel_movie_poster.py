# Generated by Django 5.0.6 on 2024-06-13 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviemodel',
            name='movie_poster',
            field=models.ImageField(blank=True, null=True, upload_to='movie_poster_img'),
        ),
    ]
