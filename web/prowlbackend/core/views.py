from rest_framework import generics, permissions, views, status
from rest_framework.response import Response
from .models import Course, Group, Code
from .serializers import CourseSerializer, GroupSerializer, CodeSerializer

from users.models import User


class CourseListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny];

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def post(self, request, *args, **kwargs):
        course = Course.objects.get(pk=request.data['id'])
        user = request.user

        operation = request.data['change']

        if operation == 'enroll':
            course.add_user(user)
        elif operation == 'unenroll':
            course.remove_user(user)
        else:
            content = {'error': '400, operation not allowed'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        group = Group(course=course)
        group.save()
        group.add_user(user)
        return Response()

class CourseDetailView(views.APIView):
    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            content = {'error': '404, course object not found'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

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
            content = {'error': '404, group object not found'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        group = self.get_object(pk)
        serializer = GroupSerializer(group, context={'request': request})
        return Response(serializer.data)

class CodeListView(generics.ListAPIView):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer

class CodeDetailView(views.APIView):
    def get_object(self, pk):
        try:
            return Code.objects.get(pk=pk)
        except Code.DoesNotExist:
            content = {'error': '404, group object not found'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        code = self.get_object(pk)
        serializer = CodeSerializer(code, context={'request': request})
        return Response(serializer.data)
