# Generated by Django 5.0.6 on 2024-06-13 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj_app', '0003_moviemodel_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviemodel',
            name='trailer_url',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
