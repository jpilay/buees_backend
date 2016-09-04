# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import backend.validators


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_auto_20160904_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(help_text='El usuario debe pertenecer a un grupo.', max_length=10, validators=[backend.validators.validate_phone_format]),
        ),
    ]
