# Generated by Django 2.2.25 on 2022-06-13 08:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnels', '0003_auto_20220613_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='date_de_maintenance',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 8, 11, 46, 888571)),
        ),
    ]