# Generated by Django 5.0.6 on 2024-06-14 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj_app', '0006_commendmodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='commendmodel',
            new_name='commentmodel',
        ),
        migrations.RenameField(
            model_name='commentmodel',
            old_name='commend',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='commentmodel',
            old_name='commend_date',
            new_name='comment_date',
        ),
    ]
