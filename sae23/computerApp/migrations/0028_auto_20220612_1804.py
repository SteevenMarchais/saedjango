# Generated by Django 2.2.25 on 2022-06-12 18:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0027_auto_20220612_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 12, 18, 4, 1, 531192)),
        ),
    ]