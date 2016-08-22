# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_driverpublication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverpublication',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterModelTable(
            name='driverpublication',
            table='driver_publication',
        ),
    ]
