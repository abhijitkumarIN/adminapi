from .models import Employee  , Company
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee 
        fields =("__all__")


class CompanySerializer(serializers.ModelSerializer):
    Emplyees = EmployeeSerializer(many=True , read_only=True)
    class Meta:
        model = Company 
        fields =("__all__")

