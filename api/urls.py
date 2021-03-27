from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from django.conf.urls import include
from .views import SongViewSet,AudioBookViewSet,PodcostViewSet

router=routers.DefaultRouter()
router.register('song',SongViewSet)
router.register('audiobook',AudioBookViewSet)
router.register('poadcost',PodcostViewSet)

urlpatterns = [
    url('', include(router.urls)),
]
