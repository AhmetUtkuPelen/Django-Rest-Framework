from django.shortcuts import render
from rest_framework import viewsets
from .serializers import*
from .models import*

# Create your views here.

class MovieViewSets(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer
    

    
class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(type='action')
    serializer_class = MovieSerializer
    


class ComedyViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(type='comedy')
    serializer_class = MovieSerializer