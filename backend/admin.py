from django.contrib import admin
from backend.models import *

class BusScheduleAdmin(admin.ModelAdmin):
  list_display = ['image']

  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 1:
      return False
    else:
      return True

admin.site.register(BusPlate)
admin.site.register(BusRoute)
admin.site.register(BusLocation)
admin.site.register(BusSchedule,BusScheduleAdmin)
