from django.urls import  path
from .views import *
urlpatterns =[
    path('company/' ,CompanyAPI.as_view() , name="company"),
    #   path('company/' ,CompanyAPI.as_view() , name="company")
]