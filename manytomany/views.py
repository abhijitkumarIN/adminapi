from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Publication, Article
from .serializers import ArticlesSerilizer, PublicationSerializer
# Create your views here.


class PublicationAPIView(APIView):
    def get(self, request, pk=None):
        if pk and not Publication.objects.filter(id=pk).exists():
            return Response({"status": False, "message": "Please provide valid id"}, status=status.HTTP_400_BAD_REQUEST)
        if pk:
            qs = Publication.objects.get(id=pk)
            serializer = PublicationSerializer(
                qs, many=False, context={"request": request})
            return Response(serializer.data)
        qs = Publication.objects.all().order_by("-id")
        serializer = PublicationSerializer(
            qs, many=True, context={"request": request})
        return Response(serializer.data)



class ArticleAPIView(APIView):
    def get(self, request, pk=None):
        if pk and not Article.objects.filter(id=pk).exists():
            return Response({"status": False, "message": "Please provide valid id"}, status=status.HTTP_400_BAD_REQUEST)

        if pk:
            qs = Article.objects.get(id=pk)
            serializer = ArticlesSerilizer(
                qs, many=False, context={"request": request})
            return Response(serializer.data)

        qs = Article.objects.all().order_by("-id")
        serializer = ArticlesSerilizer(
            qs, many=True, context={"request": request})
        return Response(serializer.data)
