from rest_framework import viewsets
from .models import *
from .serializers import *

class BusPlateViewSet(viewsets.ModelViewSet):
    queryset = BusPlate.objects.all()
    serializer_class = BusPlateSerializer


class BusRouteViewSet(viewsets.ModelViewSet):
    queryset = BusRoute.objects.all()
    serializer_class = BusRouteSerializer


class BusPositionViewSet(viewsets.ModelViewSet):
    queryset = BusPosition.objects.all()
    serializer_class = BusPositionSerializer


class BusScheduleViewSet(viewsets.ModelViewSet):
    queryset = BusSchedule.objects.all()
    serializer_class = BusScheduleSerializer
