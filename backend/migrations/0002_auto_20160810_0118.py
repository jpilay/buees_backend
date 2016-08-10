# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-10 01:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('bus_plate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BusLocation', to='backend.BusPlate')),
                ('bus_route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BusLocation', to='backend.BusRoute')),
            ],
            options={
                'verbose_name': 'Ubicación de Bus',
                'verbose_name_plural': 'Ubicaciones de Buses',
                'db_table': 'bus_location',
            },
        ),
        migrations.RemoveField(
            model_name='busposition',
            name='bus_plate',
        ),
        migrations.RemoveField(
            model_name='busposition',
            name='bus_route',
        ),
        migrations.DeleteModel(
            name='BusPosition',
        ),
    ]
