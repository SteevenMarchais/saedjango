# Generated by Django 2.2.25 on 2022-06-13 07:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructures', '0002_auto_20220613_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infrastructures',
            name='date_de_maintenance',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 7, 57, 5, 910235)),
        ),
    ]
