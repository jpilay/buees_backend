# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import backend.validators


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_auto_20160904_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=10, validators=[backend.validators.validate_phone_format]),
        ),
        migrations.AlterModelTable(
            name='userprofile',
            table='auth_user_profile',
        ),
    ]
