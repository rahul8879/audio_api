# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Song,AudioBook,Podcost

# Register your models here.
admin.site.register(Song)
admin.site.register(Podcost)
admin.site.register(AudioBook)
