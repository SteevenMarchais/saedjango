# Generated by Django 2.2.25 on 2022-06-13 08:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0006_auto_20220613_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 8, 15, 38, 892246)),
        ),
    ]
