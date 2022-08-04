from rest_framework import status
from .models import Trip
from profiles.models import DummyUser
from .serializers import TripSerializer, TripPlaceSerializer, PlaceSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

class TripDetail (APIView):
    def get(self, request, pk, *args, **kwargs):
        trip = get_object_or_404(Trip, pk=pk)
        return Response(TripPlaceSerializer(trip).data)

    def delete(self, request, pk, *args, **kwargs):
        trip = get_object_or_404(Trip, pk=pk)
        trip.delete()
        return Response({"details": f"Trip {pk} successfully deleted "}, status=status.HTTP_204_NO_CONTENT)

class TripUsers(APIView):
    '''
    Add existing users by ID to an existing trip. 
    Remove users from a trip. 
    '''
    def post(self,request,*args, **kwargs):
        trip = get_object_or_404(Trip, pk=kwargs['pk'])
        if not request.data.get('users'):
            return Response({"detail": "User list must be provided"}, status=status.HTTP_400_BAD_REQUEST)
        for id in request.data['users']:
            user = get_object_or_404(DummyUser, pk=id)
            trip.users.add(user)
        return Response(TripSerializer(trip).data, status=status.HTTP_201_CREATED)
        

    def patch(self,request, *args, **kwargs):
        trip = get_object_or_404(Trip, pk=kwargs['pk'])
        if not request.data.get('users'):
            return Response({"detail": "User list must be provided"}, status=status.HTTP_400_BAD_REQUEST)
        for id in request.data['users']:
            user = get_object_or_404(DummyUser, pk=id)
            trip.users.remove(user)

        return Response(TripSerializer(trip).data)

class TripPlaces(APIView):
    '''
    Add a new place to a trip. 
    '''
    def post(self, request, pk):
        # Retrieve trip you want to modify
        trip = get_object_or_404(Trip, pk=pk)
        request.data['trip'] = trip.id
        place = PlaceSerializer(data = request.data)
        if place.is_valid(raise_exception=True):
            place.save()

        return Response(TripPlaceSerializer(trip).data, status=status.HTTP_201_CREATED )
