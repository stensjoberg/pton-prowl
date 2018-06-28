from rest_framework import generics

from .models import Course, Group
from .serializers import CourseSerializer, GroupSerializer

class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class GroupListView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
