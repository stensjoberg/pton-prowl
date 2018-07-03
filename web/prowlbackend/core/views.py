from rest_framework import generics, permissions, views
from rest_framework.response import Response
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

        return Response()

class CourseDetailView(views.APIView):
    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        course = self.get_object(pk)
        serializer = CourseSerializer(course, context={'request': request})
        return Response(serializer.data)

class GroupListView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupDetailView(views.APIView):
    def get_object(self, pk):
        try:
            return Group.objects.get(pk=pk)
        except Group.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        group = self.get_object(pk)
        serializer = GroupSerializer(group, context={'request': request})
        return Response(serializer.data)
