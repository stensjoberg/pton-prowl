from rest_framework import generics, permissions, views
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from .permissions import IsProfileOwnerOrReadOnly

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(views.APIView):

    permission_classes = [IsProfileOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)
