from django.db import models
from django.contrib.auth.models import User, Group
import smtplib
import datetime


class BusPlate(models.Model):
    name = models.CharField(max_length=45, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bus_plate'
        verbose_name = 'Placa Bus'
        verbose_name_plural = 'Placas Buses'


class BusRoute(models.Model):
    name = models.CharField(max_length=45, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bus_route'
        verbose_name = 'Ruta Bus'
        verbose_name_plural = 'Rutas Buses'


class BusLocation(models.Model):
    bus_plate = models.ForeignKey(BusPlate,related_name='BusLocation',blank=False)
    bus_route = models.ForeignKey(BusRoute,related_name='BusLocation',blank=False)
    longitude = models.FloatField(blank=False)
    latitude = models.FloatField(blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bus_plate.name + ' - ' + self.bus_route.name

    def __unicode__(self):
        return unicode(self.bus_plate.name + ' - ' + self.bus_route.name)

    class Meta:
        db_table = 'bus_location'
        verbose_name = 'Ubicación de Bus'
        verbose_name_plural = 'Ubicaciones de Buses'


class BusSchedule(models.Model):
    image = models.ImageField(upload_to='HorarioBuses')

    class Meta:
        db_table = 'bus_schedule'
        verbose_name = 'Horario de Buses'
        verbose_name_plural = 'Horario de Buses'


class DriverPublication(models.Model):
    user_postman = models.ForeignKey(User, related_name='Publication', blank=True, null=True)
    bus_route = models.ForeignKey(BusRoute,related_name='Publication',blank=False)
    date = models.DateField(blank=False)
    description = models.TextField(blank=False)
    hour = models.TimeField(blank=False)
    image = models.ImageField(upload_to='Publications')
    status = models.BooleanField(default=False,blank=False)

    class Meta:
        db_table = 'driver_publication'
        verbose_name = 'Publicación de Conductor'
        verbose_name_plural = 'Publicaciones de Conductores'
