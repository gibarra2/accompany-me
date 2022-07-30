from rest_framework import generics, status
from profiles.models import DummyUser
from trips.serializers import UserTripSerializer, UserSerializer, TripSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

class UserList(generics.ListCreateAPIView):
    '''
    Get a list of all users. 
    Create a new user. 
    '''
    queryset = DummyUser.objects.all()
    serializer_class = UserSerializer

class UserDetail(APIView):
    '''
    Get individual user information via ID or email. 
    Update 
    '''
    def get(self, request, *args, **kwargs):
        queryset = DummyUser.objects.all() 
        filter = {}
        for field in kwargs:
            filter[field] = kwargs[field]
        user = get_object_or_404(queryset, **filter)
        serializer = UserSerializer(user)

        return Response(serializer.data)

    def patch(self,request, pk):
        user = get_object_or_404(DummyUser, pk = pk)
        serializer = UserSerializer(user, data=request.data, partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

class UserTrips(APIView):
    '''
    Get all of a specific user's trips. 
    Make a new trip associated w/ a user. 
    '''

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(DummyUser, pk=kwargs['pk'])
        serializer = UserTripSerializer(user)

        return Response(serializer.data)
    
    def post(self,request, *args, **kwargs):
        user = get_object_or_404(DummyUser, pk=kwargs['pk'])
        trip = TripSerializer(data=request.data)
        if trip.is_valid(raise_exception=True):
            trip.save()
            user.trips.add(trip.data['id'])
        return Response(UserTripSerializer(user).data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def delete_user_trip(request, *args, **kwargs):
    print(request)
    print(kwargs["trip_id"])

    trip_id = kwargs["trip_id"]

    return Response(f"Trip {trip_id} successfully deleted")

