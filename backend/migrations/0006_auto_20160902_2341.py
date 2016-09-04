# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import backend.validators


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20160822_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='busroute',
            name='toBase',
            field=models.FileField(validators=[backend.validators.validate_file_extension], upload_to='routes', help_text='Parada Uees-Base de ruta en formato "json".', blank=True),
        ),
        migrations.AddField(
            model_name='busroute',
            name='toUees',
            field=models.FileField(validators=[backend.validators.validate_file_extension], upload_to='routes', help_text='Parada Base-Uees de ruta en formato "json".', blank=True),
        ),
    ]
