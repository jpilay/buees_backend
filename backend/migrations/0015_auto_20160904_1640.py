# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import backend.validators


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_auto_20160904_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busschedule',
            name='image',
            field=models.ImageField(upload_to='schedule'),
        ),
        migrations.AlterField(
            model_name='driverpublication',
            name='image',
            field=models.ImageField(upload_to='publications'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(validators=[backend.validators.validate_phone_format], help_text='Ingrese un número de teléfono solo cuando el usuario pertenesca al grupo Coordinador(a).', max_length=10),
        ),
    ]
