from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from .models import *
from utils.utils import sendMail
# Create your views here.


class NotificationAPI(APIView):
    def get(self, request, pk=None):
        if pk and not Notification.objects.filter(id=pk).exists():
            return Response({"status": False, "message": "pelase provide valide pk "}, status=status.HTTP_400_BAD_REQUEST)
        if pk:
            qs = Notification.objects.get(id=pk)
            serializer = NotificationSerializer(
                qs, many=False, context={"request": request})
            return Response(serializer.data)
        qs = Notification.objects.all().order_by("id")
        serializer = NotificationSerializer(
            qs, many=True, context={"request": request})
        print(self.request.query_params.get("page"))
        # sendMail("saved message ", "you data has been saved ",
        #          "lenwoper@gmail.com", "abhijeetkumarlucknow@gmail.com")
        return Response(serializer.data)

    def post(self, request, pk=None):
        serializer = NotificationSerializer(data={
            "subject": request.data.get("subject"),
            "describition": request.data.get("describition"),
            "status": request.data.get("status"),
            "notification_type": request.data.get("notification_type"),
            "senting_time": request.data.get("senting_time"),
        })
        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "message": serializer.data}, status=status.HTTP_200_OK)
        return Response({"status": False, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if pk and not Notification.objects.filter(id=pk).exists():
            return Response({"status": False, "message": "pelase provide valide pk "}, status=status.HTTP_400_BAD_REQUEST)
        if pk:
            qs = Notification.objects.get(id=pk)
            serializer = NotificationSerializer(
                qs, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": True, "message": " Update succesfully "}, status=status.HTTP_200_OK)
            return Response({"status": False, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk and not Notification.objects.filter(id=pk).exists():
            return Response({"status": False, "message": "pelase provide valide pk "}, status=status.HTTP_400_BAD_REQUEST)

        qs = Notification.objects.get(id=pk)
        qs.delete()
        return Response({"status": True, "message": "Delete successfully "}, status=status.HTTP_200_OK)
