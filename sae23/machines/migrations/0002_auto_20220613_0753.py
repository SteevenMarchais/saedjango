# Generated by Django 2.2.25 on 2022-06-13 07:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 7, 53, 42, 228460)),
        ),
    ]