from rest_framework import serializers
from .models import  Publication , Article

class PublicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publication ,
        fields = ("__all__")


class ArticlesSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = Article ,
        fields = ("__all__")