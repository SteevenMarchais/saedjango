# Generated by Django 2.2.25 on 2022-06-13 10:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnels', '0013_auto_20220613_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='date_de_maintenance',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 10, 59, 54, 424804)),
        ),
    ]
