from .serializers import SingerSerializer , SongSerializer
from rest_framework import viewsets 
from .models import Singer , Song


class SingrView(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class SongSerializer(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SingerSerializer