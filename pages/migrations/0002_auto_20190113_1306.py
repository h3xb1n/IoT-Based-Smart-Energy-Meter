# Generated by Django 2.1 on 2019-01-13 07:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='energyusage',
            name='created_at',
        ),
        migrations.AddField(
            model_name='energyusage',
            name='cdate',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='energyusage',
            name='ctime',
            field=models.TimeField(default=datetime.time(13, 6, 34, 837621)),
        ),
    ]
