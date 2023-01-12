from django.urls import path 
from .views import RecurringApi


urlpatterns =[
    path("recurring/" ,RecurringApi.as_view() , name="recurring")
]