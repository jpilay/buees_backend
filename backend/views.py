from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.cache import never_cache
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


def points(request):

    try:
      stop_name = request.GET['stop_name'].strip()
      print(stop_name)
    except:
        return HttpResponseBadRequest('Error en parametros')

    data = json.loads('json/' + stop_name)
    return HttpResponse(data, mimetype='application/json', )
    #return HttpResponse(json.dumps('json/' + stop_name))
