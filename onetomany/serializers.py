from .models import Employee  , Company
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):


    class Meta:
        model = Employee 
        fields =("__all__")



class CompanySerializer(serializers.ModelSerializer):
    employee = serializers.SerializerMethodField('companyemployee')
    class Meta:
        model = Company 
        fields =("__all__")

    def companyemployee(self, obj):
        if Employee.objects.filter(company=obj.id).exists():
            qs = Employee.objects.filter(company=obj.id).order_by('-id')
            return EmployeeSerializer(qs, many=True).data
        
