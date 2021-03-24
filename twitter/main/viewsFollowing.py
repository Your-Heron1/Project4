from rest_framework import permissions, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import *
from .serializers import *
from rest_framework.views import APIView


class UserFollowingViewSet(generics.ListAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = FollowingSerializer
    queryset = Following.objects.all()


class UserFollowingCreate(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = FollowingDetailSerializer