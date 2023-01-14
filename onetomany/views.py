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
            return Response({"status": True, "company": serializer.data})
        qs = Company.objects.all().order_by("id")
        serializer = CompanySerializer(
            qs, many=True, context={"request": request})
        return Response({"status": True, "company": serializer.data})

    def post(self, request, pk=None):
        serializer = CompanySerializer(data={
            "name": request.data.get("company_name"),
            "detail": request.data.get("detail"),
            "location": request.data.get("location"),
            "about": request.data.get("about"),
            "active": request.data.get("cmpactive", False),
        })
        serializersec = EmployeeSerializer(data={
            "name": request.data.get("name"),
            "email": request.data.get("email"),
            "job_type": request.data.get("job_type"),
            "active": request.data.get("active", False),
        })
        if serializer.is_valid() and serializersec.is_valid():
            serializer.save()
            serializersec.save()
            e_obj = Employee.objects.get(id=serializersec.data.get('id'))
            e_obj.company = Company.objects.get(id=serializer.data.get('id'))
            e_obj.save()
            return Response({"status": True, "message": "Post successfully"}, status=status.HTTP_200_OK)
        return Response({"status": False, "message": dict(serializer.errors, **serializersec.errors)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if pk and not Company.objects.filter(id =pk).exists() :
            return Response({"status":False , "message":"Please provide valid pk "}, status=status.HTTP_404_NOT_FOUND)
        if pk :
            employe_id = request.data.get("employ_id")
            qs_company = Company.objects.get(id = pk )
            qs_employes = Employee.objects.get(id= int(employe_id))

            serializer_company = CompanySerializer(qs_company , data = request.data , partial= True)
            serializer_employes = EmployeeSerializer(qs_employes , data=request.data , partial=True)
            if serializer_company.is_valid() and serializer_employes.is_valid():
                serializer_company.save()
                serializer_employes.save()
                return Response({"status":True , "message":"Updated succefully" } , status=status.HTTP_200_OK)
            return Response({"status":False,"message":dict(serializer_employes.errors , **serializer_company.errors)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self , request , pk = None):
        if pk and not Company.objects.filter(id=pk).exists():
            return Response({"status":False , "message":"Please provide a valid id "} , status=status.HTTP_400_BAD_REQUEST)
   
        qs = Company.objects.get(id =pk)
        qs.delete()
        return Response({"status":True , "message":"Deleted successfully"},status=status.HTTP_200_OK)
 




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
