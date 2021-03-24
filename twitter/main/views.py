from requests import Response
from rest_framework import generics, permissions, status, authentication
from rest_framework.views import APIView

from .models import *
from .serializers import *


class Logout(APIView):
    def get(self, request):
        request.user.auth_token.delite()
        return Response(status=status.HTTP_200_OK)


class PostCreateView(generics.ListCreateAPIView):
    serializer_class = PostDetailSerializer


class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()