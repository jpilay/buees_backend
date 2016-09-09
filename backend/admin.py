from django.contrib import admin
from backend.models import *
from django.contrib.auth.admin import UserAdmin
from push_notifications.models import APNSDevice

class BusScheduleAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
          return False
        else:
          return True


class BusLocationAdmin(admin.ModelAdmin):
    list_display = ['bus_plate','bus_route', 'latitude', 'longitude', 'date']


class DriverPublicationAdmin(admin.ModelAdmin):
    list_display = ['bus_route', 'description', 'hour', 'date', 'image', 'status']


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    max_num=1


class UserAdmin(UserAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(APNSDevice)
admin.site.unregister(User)
admin.site.register(BusPlate)
admin.site.register(BusRoute)
admin.site.register(BusLocation,BusLocationAdmin)
admin.site.register(BusSchedule,BusScheduleAdmin)
admin.site.register(DriverPublication, DriverPublicationAdmin)
admin.site.register(User,UserAdmin)
