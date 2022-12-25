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
        serializer = EmployeeSerializer(data={
            "name": request.data.get("name"),
            "email": request.data.get("email"),
            "job_type": request.data.get("job_type"),
            "active": request.data.get("active"),
            "created": request.data.get("created"),
        })

        if serializer.is_valid():
            # return Response(serializer.data)
            serializer.save()
            print(serializer.data)
            serializersec = CompanySerializer(data={
                "Emplyees": serializer.data,
                "name": request.data.get("company_name"),
                "detail": request.data.get("detail"),
                "location": request.data.get("location"),
                "about": request.data.get("about"),
                 "created": request.data.get("created_compnay"),
                "active": request.data.get("cmpactive"),
            })
            if serializersec.is_valid():
                serializersec.save()
                return Response({"data":serializer.data ,"msg":" --- "})
        return Response(serializer.errors)
