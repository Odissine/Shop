from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers
# from views_api import *


router = routers.DefaultRouter()
router.register(r'especes', EspeceViewSet)
router.register(r'varietes', VarieteViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
