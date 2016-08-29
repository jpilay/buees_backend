from django.contrib import admin
from backend.models import *
from push_notifications.models import APNSDevice

class BusScheduleAdmin(admin.ModelAdmin):
  list_display = ['id', 'image']

  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 1:
      return False
    else:
      return True


class DriverPublicationAdmin(admin.ModelAdmin):
  list_display = ['bus_route', 'description', 'hour', 'date', 'image', 'status']


admin.site.unregister(APNSDevice)
admin.site.register(BusPlate)
admin.site.register(BusRoute)
admin.site.register(BusLocation)
admin.site.register(BusSchedule,BusScheduleAdmin)
admin.site.register(DriverPublication, DriverPublicationAdmin)
