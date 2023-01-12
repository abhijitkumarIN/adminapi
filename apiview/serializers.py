from rest_framework import serializers
from .models import RecurrringOrder


class ReccuringOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecurrringOrder
        fields = ("__all__")
