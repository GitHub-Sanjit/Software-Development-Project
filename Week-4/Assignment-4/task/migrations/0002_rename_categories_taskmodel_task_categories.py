# Generated by Django 4.2.8 on 2023-12-08 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskmodel',
            old_name='categories',
            new_name='task_categories',
        ),
    ]
