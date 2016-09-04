# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import backend.validators


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_auto_20160904_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(validators=[backend.validators.validate_phone_format], max_length=10),
        ),
    ]
