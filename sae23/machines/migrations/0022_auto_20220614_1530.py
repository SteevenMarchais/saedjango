# Generated by Django 2.2.25 on 2022-06-14 15:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0021_auto_20220613_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 14, 15, 30, 32, 166466)),
        ),
    ]