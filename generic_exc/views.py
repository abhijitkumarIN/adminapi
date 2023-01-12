from rest_framework.generics import *
from .serializers import SchoolSerializer
from .models import School
from .pagination import CustomPagination

'''
from rest_framework.generics import
ListAPIView , RetrieveAPIView , UpdateAPIView ,DestroyAPIView
'''

class RetrieveUpdateDestroySchoolList(RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    pagination_class= CustomPagination


class ListCreateSchoolList(ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    pagination_class=CustomPagination


# class SchoolList(ListAPIView):
#     queryset = School.objects.all()
#     serializer_class = SchoolSerializer

# class RetrieveSchoolList(RetrieveAPIView):
#     queryset = School.objects.all()
#     serializer_class = SchoolSerializer


# class UpdateSchoolList(UpdateAPIView):
#     queryset = School.objects.all()
#     serializer_class = SchoolSerializer

# class DestroySchoolList(DestroyAPIView):
#     queryset = School.objects.all()
#     serializer_class = SchoolSerializer
# # --
# class ListCreateSchoolList(ListCreateAPIView):
#     queryset = School.objects.all()
#     serializer_class = SchoolSerializer

# class RetrieveUpdateSchoolList(RetrieveUpdateAPIView):
#     queryset = School.objects.all()
#     serializer_class = SchoolSerializer

# class RetrieveDestroySchoolList(RetrieveDestroyAPIView):
#     queryset = School.objects.all()
#     serializer_class = SchoolSerializer



# class RetrieveUpdateDestroySchoolList(RetrieveUpdateDestroyAPIView):
#     queryset = School.objects.all()
#     serializer_class = SchoolSerializer
# class DestroySchoolList():
#     queryset = School.objects.all()
#     serializer_class = SchoolSerializer

