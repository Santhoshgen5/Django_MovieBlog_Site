# Generated by Django 5.0.6 on 2024-06-14 05:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj_app', '0005_alter_moviemodel_director'),
    ]

    operations = [
        migrations.CreateModel(
            name='commendmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('commend', models.TextField()),
                ('commend_date', models.DateTimeField(auto_now=True)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proj_app.moviemodel')),
            ],
        ),
    ]
