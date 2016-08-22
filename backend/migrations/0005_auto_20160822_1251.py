# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20160822_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverpublication',
            name='date',
            field=models.DateField(),
        ),
    ]
