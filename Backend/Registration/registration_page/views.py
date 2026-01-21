from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics

# Create your views here.
class Register(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UpdateRegister(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer