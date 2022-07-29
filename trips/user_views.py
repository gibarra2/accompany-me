from rest_framework import generics, status
from urllib3 import HTTPResponse
from profiles.models import DummyUser
from trips.serializers import UserTripSerializer, UserMinSerializer, TripSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

class UserList(generics.ListCreateAPIView):
    '''
    Get a list of all users. 
    Create a new user. 
    '''
    queryset = DummyUser.objects.all()
    serializer_class = UserMinSerializer


class MultipleFieldLookupMixin:
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self):
        queryset = self.get_queryset()             
        queryset = self.filter_queryset(queryset)  
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs.get(field, None):  
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj


class UserDetail(MultipleFieldLookupMixin, generics.RetrieveUpdateAPIView):
    '''
    '''
    queryset = DummyUser.objects.all()
    serializer_class = UserMinSerializer
    lookup_fields = ['pk', 'email']

    def put(self, request, *args, **kwargs):
        pass

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
            user.trips.add(trip.data["id"])
        return Response(UserTripSerializer(user).data, status=status.HTTP_201_CREATED)

