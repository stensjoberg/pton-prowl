from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['netid', 'email', 'full_name', 'class_year']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='users:user-detail',
        lookup_field='pk'
    )

    class Meta:
        model = User
        fields = ['url', 'netid', 'email', 'full_name', 'class_year']
