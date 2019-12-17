from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics 
from django.shortcuts import get_object_or_404

from tutorials.models import Tutorial, Module
from .serializers import TutorialSerializer, TutorialDetailSerializer

# Create your views here.
class TutorialList(generics.ListAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer

class TutorialDetail(generics.ListAPIView):
    pass
    # queryset = Tutorial.objects.all()
    # serializer_class = TutorialDetailSerializer