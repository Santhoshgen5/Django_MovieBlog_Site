# Generated by Django 5.0.6 on 2024-06-17 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj_app', '0010_remove_moviemodel_sample'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviemodel',
            name='sample',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]