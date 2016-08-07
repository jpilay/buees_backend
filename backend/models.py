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


class BusPosition(models.Model):
    bus_plate = models.ForeignKey(BusPlate,related_name='BusPosition',blank=False)
    bus_route = models.ForeignKey(BusRoute,related_name='BusPosition',blank=False)
    longitude = models.FloatField(blank=False)
    latitude = models.FloatField(blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bus_plate.name + ' - ' + self.bus_route.name

    def __unicode__(self):
        return unicode(self.bus_plate.name + ' - ' + self.bus_route.name)

    class Meta:
        db_table = 'bus_position'
        verbose_name = 'Posición de Bus'
        verbose_name_plural = 'Posiciones de Buses'


class BusSchedule(models.Model):
    image = models.ImageField(upload_to='HorarioBuses')

    class Meta:
        db_table = 'bus_schedule'
        verbose_name = 'Horario de Buses'
        verbose_name_plural = 'Horario de Buses'


'''
def send_email(modeloAsunto,usuario,clave,recipient):

    # Setup email

    sender = 'bueesproyecto@gmail.com'
    subject = modeloAsunto
    body = '<br><br>Usuario: ' + usuario + '<br>Clave: ' + clave
    headers = ["From: " + sender,
               "Subject: " + subject,
               "To: " + recipient,
               "MIME-Version: 1.0",
               "Content-Type: text/html"]
    headers = "\r\n".join(headers)

    # SMTP credentials
    password = 'buees2015'

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender, password)

    # Send email
    server.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
    server.quit()
'''
