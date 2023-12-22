# Generated by Django 4.2.8 on 2023-12-22 06:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 12, 22, 6, 1, 27, 79670, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobpost',
            name='description',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobpost',
            name='salary',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
