from django.urls import path
from .views import LatestProductDataSearch , LatestProductData
# Create your views here.


urlpatterns = [
    path('latestproduct/',LatestProductData.as_view(), name=''),
    path('latestproductsearch/',LatestProductDataSearch.as_view(), name='')
]
