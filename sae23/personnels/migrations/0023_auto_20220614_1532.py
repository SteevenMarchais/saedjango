# Generated by Django 2.2.25 on 2022-06-14 15:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnels', '0022_auto_20220614_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='date_de_maintenance',
            field=models.DateField(default=datetime.datetime(2022, 6, 14, 15, 32, 18, 945718)),
        ),
    ]
