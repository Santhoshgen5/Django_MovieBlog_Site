# Generated by Django 5.0.6 on 2024-06-17 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj_app', '0008_moviemodel_sample'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviemodel',
            name='sample',
            field=models.CharField(max_length=20, null=True),
        ),
    ]