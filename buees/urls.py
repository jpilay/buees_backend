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
from django.conf.urls import url, include
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
router.register(r'Coordinator', CoordinatorViewSet)
router.register(r'DriverPublication', DriverPublicationViewSet)
router.register(r'UserGroup', UserGroupViewSet)

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^bus_location/', bus_location, name='bus_location'),
    url(r'^delivery/', delivery, name='delivery'),
    url(r'^notify/', notify, name='notify'),
    url(r'^recovery_password/', recovery_password, name='recovery_password'),
    url(r'^register_device/', register_device, name='register_device'),
    url(r'^signin/', signin, name='signin'),
    url(r'^signup/', signup, name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
