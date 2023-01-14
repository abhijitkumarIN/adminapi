from django.shortcuts import render
from rest_framework.generics import *
from .models import LatestProducts
from .serializers import LatestProductSerializer
from rest_framework import filters


class LatestProductDataSearch(ListAPIView):
    queryset = LatestProducts.objects.all()
    serializer_class = LatestProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['describition']


class LatestProductData(ListCreateAPIView):
    queryset = LatestProducts.objects.all()
    serializer_class =LatestProductSerializer
    # pagination_class=CustomPagination
