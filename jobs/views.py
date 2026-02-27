from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import job
from .serializers import Jobserializer
from .permissions import IsEmployee

# Create your views here.
class JobCreateView(generics.CreateAPIView):
    queryset = job.objects.all()
    serializer_class = Jobserializer
    permission_classes = [IsAuthenticated,IsEmployee]

    def perform_create(self, serializer):
       serializer.save(created_by=self.request.user)