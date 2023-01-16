from .models import Collage, Student
from rest_framework import serializers
import json
class StudentSerializer(serializers.ModelField):
    class Meta:
        model = Student
        fields = ("__all__")


class CollageSerializer(serializers.ModelSerializer):
    collage = serializers.SerializerMethodField('collage_student')

    class Meta:
        model = Collage
        fields = ("__all__")

    def collage_student(self, object):
        if Student.objects.filter(collage=object.id).exists():
            qs = Student.objects.filter(collage=object.id).order_by('-id')
            return StudentSerializer(qs , many=True).data
           
