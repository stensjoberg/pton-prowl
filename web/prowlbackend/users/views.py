from rest_framework import generics, permissions, views
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from .permissions import IsProfileOwnerOrReadOnly

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(views.APIView):

    permission_classes = [IsProfileOwnerOrReadOnly]
    def get(self, request, pk, format=None):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)

class ValidateView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    # minimal overhead view for checking if user is validated by request
