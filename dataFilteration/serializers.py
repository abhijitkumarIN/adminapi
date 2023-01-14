from .models import LatestProducts
from rest_framework import serializers


class LatestProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatestProducts
        fields =("__all__")