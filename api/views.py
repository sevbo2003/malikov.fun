from rest_framework import generics
from .serializers import CustomUserApi
from accounts.models import CustomUser


class CustomUserApiView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserApi


class CustomUserDetailApiView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserApi
