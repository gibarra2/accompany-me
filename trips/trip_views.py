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

