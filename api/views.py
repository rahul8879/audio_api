# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .models import Song,AudioBook,Podcost
from .serializers import SongSerlizers,AudioBookSerlizers,PodcostSerlizers

# Create your views here.

class SongViewSet(viewsets.ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerlizers


class AudioBookViewSet(viewsets.ModelViewSet):
    queryset=AudioBook.objects.all()
    serializer_class=AudioBookSerlizers

class PodcostViewSet(viewsets.ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=PodcostSerlizers
