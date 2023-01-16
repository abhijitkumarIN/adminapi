from django.urls import path
from .views import CollageApi
urlpatterns =[
    path("collage/" ,CollageApi.as_view() ,name="collage"),
     path("collage/<int:pk>" ,CollageApi.as_view() ,name="collage")
]