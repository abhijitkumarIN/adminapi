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
            serializer = CompanySerializer(comp_obj, many=False, context={"request": request})
            return Response({"status":True, "company":serializer.data})
        qs = Company.objects.all().order_by("id")
        serializer = CompanySerializer(
            qs, many=True, context={"request": request})
        return Response({"status":True, "company":serializer.data})

    def post(self, request, pk=None):

        serializer = CompanySerializer(data={

            "name": request.data.get("company_name"),
            "detail": request.data.get("detail"),
            "location": request.data.get("location"),
            "about": request.data.get("about"),
            "active": request.data.get("cmpactive", False),
        })
        # print(serializer)

        serializersec = EmployeeSerializer(data={
            # "company": serializer.data.get('id'),
            "name": request.data.get("name"),
            "email": request.data.get("email"),
            "job_type": request.data.get("job_type"),
            "active": request.data.get("active", False),
        })

        if serializer.is_valid() and serializersec.is_valid():
            serializer.save()
            serializersec.save()
            e_obj = Employee.objects.get(id=serializersec.data.get('id'))
            e_obj.company=Company.objects.get(id=serializer.data.get('id'))
            e_obj.save()
            return Response({"status": True, "message": "Post successfully"}, status=status.HTTP_200_OK)

        return Response({"status": False, "message": dict(serializer.errors, **serializersec.errors)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):

        serializer_obj = CompanySerializer(data={request.data}, partial=True)
        if serializer_obj.is_valid():
            serializer_obj.save()


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
