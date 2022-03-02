<<<<<<< HEAD
from rest_framework import generics, permissions
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User
from snippets.permissions import IsOwnerOrReadOnly
=======
from rest_framework import generics  
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User

from tutorial.snippets.serializers import UserSerializer

>>>>>>> a4779cb9088c4c35e3a403b4acf0318674da38b1

# Create your views here.

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

<<<<<<< HEAD
=======
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

>>>>>>> a4779cb9088c4c35e3a403b4acf0318674da38b1
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
