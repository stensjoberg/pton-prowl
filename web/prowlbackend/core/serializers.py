from rest_framework import serializers
from .models import Course, Group
from users.serializers import UserSerializer

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='core:group-detail',
        lookup_field='pk'
    )

    users = serializers.HyperlinkedRelatedField(
        view_name='users:user-detail',
        lookup_field='pk',
        many=True,
        read_only=True
    )

    course = serializers.HyperlinkedRelatedField(
        view_name='core:course-detail',
        lookup_field='pk',
        many=False,
        read_only=True
    )

    class Meta:
        model = Group
        fields = ['url', 'id', 'course', 'users']

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='core:course-detail',
        lookup_field='pk'
    )

    users = serializers.HyperlinkedRelatedField(
        view_name='users:user-detail',
        lookup_field='pk',
        many=True,
        read_only=True
    )

    groups = serializers.HyperlinkedRelatedField(
        view_name='core:group-detail',
        lookup_field='pk',
        many=True,
        read_only=True
    )


    class Meta:
        model = Course
        fields = ['url', 'id', 'title', 'groups', 'users']
