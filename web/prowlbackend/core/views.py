from rest_framework import generics, permissions
from django.http import HttpResponse
from .models import Course, Group
from .serializers import CourseSerializer, GroupSerializer

from users.models import User


class CourseListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny];

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def post(self, request, *args, **kwargs):
        course = Course.objects.get(pk=request.data['id'])
        user = request.user
        course.add_user(user)

        group = Group(course=course)
        group.save()
        group.add_user(user)

        return HttpResponse()

class GroupListView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
