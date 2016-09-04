from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from push_notifications.models import GCMDevice
from .models import *
import json


# Map
def index(request):
    routes = BusRoute.objects.all()
    context = {'routes':routes,}
    return render(request, 'map.html', context)


# View looking the last location of bus
@never_cache
def bus_location(request):
    response = {}

    try:
    	  bus_route_name = request.GET['bus_route'].strip()
    except:
        return HttpResponseBadRequest('Error en parametros')

    r = BusRoute.objects.get(name=bus_route_name)
    query = BusLocation.objects.filter(bus_route=r).order_by('-id')

    if query:
        query = query.first()
        response = {'plate':query.bus_plate.name,'latitude': query.latitude,'longitude':query.longitude,'route':query.bus_route.name}

    return HttpResponse(json.dumps(response))


# Generate new password
def generate_password():
    import random,string
    new_pwd = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5))
    return new_pwd


# Save information device for Notification Push
@csrf_exempt
def register_device(request):

    response = {}
    username = request.POST.get('username',None)
    device_id = request.POST.get('device_id',None)
    registration_id = request.POST.get('registration_id',None)

    if username and device_id and registration_id:
        gcm_device = GCMDevice.objects.filter(device_id=device_id)

        if gcm_device:
            gcm_device = gcm_device.firts()

        else:
            user = User.objects.get(username=username)
            gcm_device = GCMDevice.objects.create(user=user,name=username,device_id=device_id,registration_id=registration_id)
            gcm_device.save()

        response = {'id':gcm_device.id,}

    return JsonResponde(response)


# Change password of user
@csrf_exempt
def recovery_password(request):
    response = {}
    username = request.POST.get('username', None)
    new_password = request.POST.get('password', None)

    if username:
        user = User.objects.filter(username=username)

        if user:

            if not new_password:
                new_password = generate_password()

            user = user.first()
            user.set_password(new_password)
            user.save()
            group = Group.objects.get(user=user)

            from django.conf import settings
            try:
                send_mail(
                    'Cambio de clave',
                    '',
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    html_message = recovery_password_email(user.username,new_password)
                    )
            except:
                print(user.username + ': Don\'t send recovery password email!')

            response = {'username':user.username, 'email':user.email, 'group':group.name}

    return JsonResponse(response)


# Email message for recovery password of user
def recovery_password_email(username,password):
    body = '<table align="center"><thead><tr><td style="background-color:#ffffff;padding-left:20px"><img style="width: 164px; height: 42px;"  alt="icono"  src="http://www.uees.edu.ec/images/logo-uees.jpg"></td></tr></thead><tbody><tr><td style="padding:20px"><div  style="text-align: left;"><br>Hola ' + username + '!<br><br>Has solicitado restablecer la contrase&ntilde;a de tu cuenta de Buees,<br><br><span style="font-weight: bold;">Contrase&ntilde;a: </span>' + password + '<br><br>En caso que desees cambiar la contrase&ntilde;a, puedes ir al bot&oacute;n de cambiar contrase&ntilde;a que <br>se encuentra en ajustes del menu principal.<br><br><br>Gracias,<br>El equipo de Buues<br><br></div></td></tr><tr><td style="background-color:#eeeeee;"></div></td></tr></tbody></table>'

    return body


# Sign in to application
@csrf_exempt
def signin(request):
    response = {}
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)

    if username and password:
        user = authenticate(username=username, password=password)

        if user:
            registration_id = ''
            group = Group.objects.filter(user=user)
            gcm_device = GCMDevice.objects.filter(user=user.id)

            if gcm_device:
                gcm_device = gcm_device.firts()
                registration_id = gcm_device.registration_id

            if group:
                group = group.first()
                response = {'username':user.username, 'email':user.email, 'group':group.name, 'registration_id':registration_id}

    return JsonResponse(response)


# Sign up to application
@csrf_exempt
def signup(request):
    response = {}
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    email = request.POST.get('email', None)
    group_name = request.POST.get('group_name', None)

    if username and password and email:
        user = User.objects.filter(username=username)
        group = Group.objects.filter(name=group_name)

        if not user and group:
            user = User.objects.create_user(username,email,password)
            group = group.first()
            user.groups.add(group)
            user.save()

            from django.conf import settings
            try:
                send_mail(
                    'Bienvenido(a)!',
                    '',
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    html_message = signup_email(user.username)
                    )
            except:
                print(user.username + ': Don\'t send welcome email!')

            response = {'username':user.username, 'email':user.email, 'group':group.name}

    return JsonResponse(response)


# Email message for welcome of user
def signup_email(username):
    body = '<table align="center"><thead><tr><td style="background-color:#ffffff;padding-left:20px"><img  style="width: 164px; height: 42px;"  alt="icono"  src="http://www.uees.edu.ec/images/logo-uees.jpg"></td></tr></thead><tbody><tr><td  style="padding:20px"><div>Hola ' + username + '!<br><br>Hemos asegurado que tenemos correctamente tu correo electr&oacute;nico.<br><span  style="font-weight: bold;">Ahora podras acceder a la aplicaci&iacute;n y disfrutar de todas las opciones que tiene para t&iacute;.</div><br><br/>Gracias,<br>El equipo Buees</div></td></tr><tr><td style="background-color:#eeeeee;"></div></td></tr></tbody></table>'

    return body
