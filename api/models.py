# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
class Song(models.Model):
    songName=models.CharField(unique=True,max_length=100,null=False)
    duration=models.PositiveIntegerField(null=False)
    uploadedTime=models.DateTimeField(auto_now=False, auto_now_add=False)



class Podcost(models.Model):

    podcost_name=models.CharField(unique=True,max_length=100,null=False)
    duration=models.PositiveIntegerField(null=False)
    uploadedTime=models.DateTimeField(auto_now=False, auto_now_add=False)
    host=models.CharField(unique=True,max_length=100,null=False)



class AudioBook(models.Model):
    title=models.CharField(unique=True,max_length=100,null=False)
    author=models.CharField(unique=True,max_length=100,null=False)
    narrator=models.CharField(unique=True,max_length=100,null=False)
    duration=models.PositiveIntegerField(null=False)
    uploadedTime=models.DateTimeField(auto_now=False, auto_now_add=False)
