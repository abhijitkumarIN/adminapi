from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EmployeeSerializer, CompanySerializer
from .models import *
# Create your views here.


class CompanyAPI(APIView):
    def get(self, request, pk=None):
        if pk and not Company.objects.filter(id=pk).exists():
            return Response({"status": False, "msg": "Please provide valid pk "}, status=status.HTTP_400_BAD_REQUEST)
        if pk:
            comp_obj = Company.objects.get(id=pk)
            serializer = CompanySerializer(
                comp_obj, many=False, context={"request": request})
            return Response(serializer.data)
        qs = Company.objects.all().order_by("id")
        serializer = CompanySerializer(
            qs, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request, pk=None):
        serializer = CompanySerializer(data={

            "name": request.data.get("company_name"),
            "detail": request.data.get("detail"),
            "location": request.data.get("location"),
            "about": request.data.get("about"),
            "active": request.data.get("cmpactive",False),
        })
        # print(serializer)


        if serializer.is_valid():
            company_serializer=serializer.save()
            print(company_serializer)
        else:
            return Response(serializer.errors)

        print(serializer.data)

        serializersec = EmployeeSerializer(data={
            "company": serializer.data.get('id'),
            "name": request.data.get("name"),
            "email": request.data.get("email"),
            "job_type": request.data.get("job_type"),
            "active": request.data.get("active",False),
        })

        if serializersec.is_valid():
            employee_serializersec=serializersec.save()
            print(employee_serializersec,"===> second serializer")
            return Response({"company_data": serializer.data, "employee_data":EmployeeSerializer(employee_serializersec).data,"msg": " --- "})
        else:
            return Response({"serializersec":serializersec.errors})


class EmployeeAPI(APIView):
    def get(self, request, pk=None):
        if pk and not Employee.objects.filter(id=pk).exists():
            return Response({"status": False, "msg": "Please provide valid pk "}, status=status.HTTP_400_BAD_REQUEST)
        if pk:
            comp_obj = Employee.objects.get(id=pk)
            serializer = EmployeeSerializer(
                comp_obj, many=False, context={"request": request})
            return Response(serializer.data)
        qs = Employee.objects.all().order_by("id")
        serializer = EmployeeSerializer(
            qs, many=True, context={"request": request})
        return Response(serializer.data)
