from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *


class ProfileCreateView(generics.ListCreateAPIView):
    serializer_class = ProfileDetailSerializer


class ProfileListView(generics.ListAPIView):
    serializer_class = ProfileListSerializer
    queryset = Profile.objects.all()


class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileDetailSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()
