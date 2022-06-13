# Generated by Django 2.2.25 on 2022-06-13 08:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructures', '0006_auto_20220613_0813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infrastructures',
            name='List_machine',
        ),
        migrations.RemoveField(
            model_name='infrastructures',
            name='List_personnel',
        ),
        migrations.AlterField(
            model_name='infrastructures',
            name='date_de_maintenance',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 8, 15, 38, 892999)),
        ),
        migrations.DeleteModel(
            name='Tag1',
        ),
        migrations.DeleteModel(
            name='Tag2',
        ),
    ]