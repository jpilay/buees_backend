from backend.models import *
from rest_framework import serializers


class BusPlateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusPlate
        fields = ('name','date')


class BusRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusPlate
        fields = ('name','date')


class BusLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusLocation
        fields = ('bus_plate', 'bus_route', 'longitude','latitude','date')


class BusScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusSchedule
        fields = ('image',)


class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)
