# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0002_auto_20160810_0118'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverPublication',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('hour', models.TimeField()),
                ('image', models.ImageField(upload_to='Publications')),
                ('status', models.BooleanField(default=False)),
                ('bus_route', models.ForeignKey(related_name='Publication', to='backend.BusRoute')),
                ('user_postman', models.ForeignKey(blank=True, null=True, related_name='Publication', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Publicaciones de Conductores',
                'db_table': 'driver publication',
                'verbose_name': 'Publicación de Conductor',
            },
        ),
    ]
