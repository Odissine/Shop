# Generated by Django 4.0.6 on 2022-07-12 15:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_inventaire_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventaire',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 7, 15, 51, 34, 646723)),
        ),
    ]
