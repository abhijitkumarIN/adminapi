from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CollageSerializer, StudentSerializer
from .models import Collage, Student

# Create your views here.


class CollageApi(APIView):
    def get(self, request, pk=None):
        if pk and not Collage.objects.filter(id=pk).exists():
            return Response({"status": False, "message": "Please provide valide pk "}, status=status.HTTP_400_BAD_REQUEST)
        if pk:
            qs = Collage.objects.get(id=pk)
            serializer = CollageSerializer(
                qs, many=False, context={"request": request})
            return Response(serializer.data)
        qs = Collage.objects.all().order_by("id")
        serializer = CollageSerializer(
            qs, many=True, context={"request": request})
        return Response(serializer.data)
