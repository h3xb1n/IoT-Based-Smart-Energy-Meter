# Generated by Django 2.1 on 2019-01-13 09:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20190113_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energyusage',
            name='ctime',
            field=models.TimeField(default=datetime.time(14, 52, 16, 599019)),
        ),
    ]
