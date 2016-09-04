# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import backend.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0007_auto_20160902_2341'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('phone', models.CharField(max_length=10)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='busroute',
            name='toBase',
            field=models.FileField(help_text='Parada Uees-Base en formato "json".', upload_to='routes', validators=[backend.validators.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='busroute',
            name='toUees',
            field=models.FileField(help_text='Parada Base-Uees en formato "json".', upload_to='routes', validators=[backend.validators.validate_file_extension]),
        ),
    ]
