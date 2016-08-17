"""buees URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from backend.viewsets import *
from backend.views import *


admin.autodiscover()
router = routers.DefaultRouter()
router.register(r'BusPlate', BusPlateViewSet)
router.register(r'BusRoute', BusRouteViewSet)
router.register(r'BusLocation', BusLocationViewSet)
router.register(r'BusSchedule', BusScheduleViewSet)

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^bus_location/', bus_location, name='bus_location'),
    url(r'^signin/', signin, name='signin'),
    url(r'^signup/', signup, name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
