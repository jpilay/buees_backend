from django.db import models
import smtplib
import datetime

'''
class CaUsuario(models.Model):
    usuario = models.CharField(max_length=45, blank=True,unique = True, primary_key=True)
    clave = models.CharField(max_length=45, blank=True)
    rol = models.CharField(max_length=45, blank=True)
    correo = models.CharField(max_length=45, blank=True,unique = True)

    def __init__(self, *args, **kwargs):
        super(CaUsuario, self).__init__(*args, **kwargs)

        try:
          self.__original_clave = self.clave

        except:
          self.__original_clave = None


    def save(self, *args, **kwargs):

        correo = self.correo
        #Envio de mail: Modificando la contrasena
        if self.__original_clave != self.clave:
            self.__original_clave = self.clave
            #self.fecha = datetime.datetime.today()
            modeloAsunto= "Cambio de Contrasena para BuessApp"
            send_email(modeloAsunto,self.usuario,self.clave,correo)

        else:
            modeloAsunto="Clave para BuessApp"
            send_email(modeloAsunto,self.usuario,self.clave,correo)

        super(CaUsuario, self).save(*args, **kwargs)

    def __str__(self):
        return self.usuario

    def __unicode__(self):
        return unicode(self.correo)

    class Meta:
        db_table = 'ca_usuario'
'''

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
