# Generated by Django 2.2.25 on 2022-06-12 09:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0018_auto_20220612_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 12, 9, 3, 33, 501541)),
        ),
    ]
