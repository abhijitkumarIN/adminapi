from .models import Employee  , Company
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):


    class Meta:
        model = Employee 
        fields =("__all__")



class CompanySerializer(serializers.ModelSerializer):
    company = serializers.SerializerMethodField('companyemployee')
    def companyemployee(self, obj):
        if Employee.objects.all().exists():
            qs = Employee.objects.all(),
            return EmployeeSerializer(qs, many=True)
        return None
    class Meta:
        model = Company 
        extra_fields=('company',)
        fields =("__all__")

