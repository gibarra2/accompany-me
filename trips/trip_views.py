from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Trip
from .serializers import TripSerializer
from rest_framework.generics import ListCreateAPIView

# Create your views here.
# GET all trips
# POST New Trip
# 
class TripList(ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

