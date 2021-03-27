from rest_framework import serializers
from .models import AudioBook,Song,Podcost

class SongSerlizers(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields=('id','songName','duration','uploadedTime')

class AudioBookSerlizers(serializers.ModelSerializer):
    class Meta:
        model=AudioBook
        fields=('id','podcost_name','duration','uploadedTime','host')

class PodcostSerlizers(serializers.ModelSerializer):
    class Meta:
        model=Podcost
        fields=('id','title','author','narrator','duration','uploadedTime')
