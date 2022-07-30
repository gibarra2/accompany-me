from rest_framework import generics, status
from .models import Trip
from .serializers import TripSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Delete a trip
@api_view(['DELETE'])
def delete_trip(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    trip.delete()
    return Response({"details": f"Trip {pk} successfully deleted "}, status=status.HTTP_204_NO_CONTENT)


# Get all users associated w/ a trip /trips/<id>/users
# Add a user to a trip trips/trip_id/users/user_id
