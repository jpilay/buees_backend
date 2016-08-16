from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from .models import *
import json


def index(request):
    routes = BusRoute.objects.all()
    context = {'routes':routes,}
    return render(request, 'map.html', context)


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


def recovery_password_email(username,password):
    body = '<table align="center"><thead><tr><td style="background-color:#eeeeee;padding:20px"><img style="width: 164px; height: 42px;"  alt="icono"  src="http://159.203.99.117:9999/media/silour/logosilour.png"></td></tr></thead><tbody><tr><td style="padding:20px"><div  style="text-align: left;"><br>Hola ' + username + '!<br><br>Has solicitado restablecer la contrase&ntilde;a de tu cuenta de Buees,<br><br><span style="font-weight: bold;">Contrase&ntilde;a: </span>' + password + '<br><br>En caso que desees cambiar la contrase&ntilde;a, puedes ir al bot&oacute;n de cambiar contrase&ntilde;a que <br>se encuentra en la opci&oacute;n de registrar.<br><br><br>Gracias,<br>El equipo de Buues<br><br></div></td></tr><tr><td style="background-color:#eeeeee;"></div></td></tr></tbody></table>'

    return body

@csrf_exempt
def signin(request):

    username = request.POST.get('username', None)
    password = request.POST.get('password', None)

    if username and password:
        context = {}
        user = authenticate(username=username, password=password)

        if user:
            group = Group.objects.filter(user=user)

            if group:
                group = group.first()
                context = {'username':user.username, 'email':user.email, 'group':group.name}

        return JsonResponse(context)
    else:
        return HttpResponseBadRequest('Error en parametros')


def welcome_email(username):
    body = '<table align="center"><thead><tr><td style="background-color:#eeeeee;padding:20px"><img  style="width: 164px; height: 42px;"  alt="icono"  src="http://159.203.99.117:9999/media/silour/logosilour.png"></td></tr></thead><tbody><tr><td  style="padding:20px"><div>Hola ' + username + '!<br><br>Hemos asegurado que tenemos correctamente tu correo electr&oacute;nico.<br><span  style="font-weight: bold;">Ahora podras acceder a la aplicaci&iacute;n y disfrutar de todas las opciones que tiene para t&iacute;.</div><br><br/>Gracias,<br>El equipo Buees</div></td></tr><tr><td style="background-color:#eeeeee;"></div></td></tr></tbody></table>'

    return body
