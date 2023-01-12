from django.urls import path
from .views import ListCreateSchoolList , RetrieveUpdateDestroySchoolList
urlpatterns = [
    path('school/', ListCreateSchoolList.as_view(), name="school"),
    path('school/<int:pk>/', RetrieveUpdateDestroySchoolList.as_view(), name="school"),
]
