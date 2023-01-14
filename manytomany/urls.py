from django.urls import path
from .views import PublicationAPIView, ArticleAPIView

urlpatterns = [
    path('publication/', PublicationAPIView.as_view(), name="publication"),
    path('articles/', ArticleAPIView.as_view(), name="articles"),
]
