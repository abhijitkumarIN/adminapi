from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import RecurrringOrder
from .serializers import RecurringOrderSerializer
# from rest_framework.
# Create your views here.


class RecurringApi(APIView):
    def get(self, request, pk=None):
        if pk and not RecurrringOrder.object.filter(id=pk).exits():
            return Response({"statu": False, "msg": "Please provide a valid ID "}, status=status.HTTP_401_UNAUTHORIZED)
        if pk:
            qs = RecurrringOrder.objects.get(id=pk)
            serializer = RecurringOrderSerializer(
                qs, many=False, context={"request": request})
            return Response(serializer.data)
        qs = RecurrringOrder.objects.all().order_by("id")
        serializer = RecurringOrderSerializer(
            qs, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request, pk=None):
        serializer = RecurringOrderSerializer(data={
            "data": request.data.get(""),
            "data": request.data.get(""),
            "data": request.data.get(""),
        })

        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "msg": "Success"}, status=status.HTTP_200_OK)
        return Response({"status": False, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if pk and not RecurrringOrder.objects.filter(id=pk).exists():
            return Response({"status": False, "msg": "Please provide Valid id "}, status=status.HTTP_400_BAD_REQUEST)
        if pk:
            qs = RecurrringOrder.objects.get(id=pk)
            serializer = RecurringOrderSerializer(
                qs, data=request.data, partial=True)
            if serializer.is_valid():
                return Response({"status": False, "msg": "Updated sucessfully "}, status=status.HTTP_200_OK)
            return Response({"status": False, "msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
