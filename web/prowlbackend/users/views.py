from rest_framework import generics, permissions, views
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from .permissions import IsProfileOwner

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(views.APIView):

    #permission_classes = [IsProfileOwner]
    def get(self, request, pk, format=None):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)

class ValidateView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = UserSerializer(request.user, context={'request': request})
        return Response(user.data)
    # minimal overhead view for checking if user is validated by request
