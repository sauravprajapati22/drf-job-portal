from django.shortcuts import render
from rest_framework import generics
from accounts.serializers import Registerserializer
from accounts.models import CustomUser
from rest_framework.permissions import AllowAny
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class  = Registerserializer
    permission_classes = [AllowAny]