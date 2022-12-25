from django.urls import path 
from .views import NotificationAPI
urlpatterns =[
    path("notification/" , NotificationAPI.as_view() ,name="notification"),
    path("notification/<int:pk>" , NotificationAPI.as_view() ,name="notification")
]