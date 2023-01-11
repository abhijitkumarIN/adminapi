from rest_framework import serializers
from .models import *
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields =("__all__")


class SingerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Singer
        fields =("__all__")