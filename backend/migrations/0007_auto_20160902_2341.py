# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import backend.validators


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20160902_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busroute',
            name='toBase',
            field=models.FileField(help_text='Parada Uees-Base de ruta en formato "json".', upload_to='routes', validators=[backend.validators.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='busroute',
            name='toUees',
            field=models.FileField(help_text='Parada Base-Uees de ruta en formato "json".', upload_to='routes', validators=[backend.validators.validate_file_extension]),
        ),
    ]
