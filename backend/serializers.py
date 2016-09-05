from backend.models import *
from rest_framework import serializers, generics


class BusPlateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusPlate


class BusRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusRoute


class BusLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusLocation
        fields = ('bus_plate', 'bus_route', 'longitude','latitude','date')


class BusScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusSchedule
        fields = ('image',)


class DriverPublicationSerializer(serializers.ModelSerializer):
    class Meta:
        #depth = 1
        model = DriverPublication
        fields = ('id', 'bus_route', 'date', 'description', 'hour', 'image')


class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)

class CoordinatorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    class Meta:
        model = UserProfile
        fields = ('username', 'phone')
