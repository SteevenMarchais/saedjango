# Generated by Django 2.2.25 on 2022-06-14 15:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0023_auto_20220614_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 14, 15, 32, 50, 347539)),
        ),
    ]