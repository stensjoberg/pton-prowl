from rest_framework import serializers
from .models import Course, Group
from users.serializers import UserSerializer

class GroupSerializer(serializers.ModelSerializer):
    users = UserSerializer(read_only=True, many=True)
    course = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'course', 'users']

class CourseSerializer(serializers.ModelSerializer):
    users = UserSerializer(read_only=True, many=True)
    groups = GroupSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'groups', 'users']
