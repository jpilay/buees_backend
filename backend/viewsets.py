from rest_framework import viewsets
from .models import *
from .serializers import *

class BusPlateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BusPlate.objects.all()
    serializer_class = BusPlateSerializer


class BusRouteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BusRoute.objects.all()
    serializer_class = BusRouteSerializer


class BusLocationViewSet(viewsets.ModelViewSet):
    queryset = BusLocation.objects.all()
    serializer_class = BusLocationSerializer


class BusScheduleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BusSchedule.objects.all()
    serializer_class = BusScheduleSerializer


class DriverPublicationViewSet(viewsets.ModelViewSet):
    queryset = DriverPublication.objects.filter(status=False)
    serializer_class = DriverPublicationSerializer


class UserGroupViewSet(viewsets.ReadOnlyModelViewSet):
    from django.db.models import Q
    queryset = Group.objects.filter(~Q(name__icontains='coordinador'))
    serializer_class = UserGroupSerializer
