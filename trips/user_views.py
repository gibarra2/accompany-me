from rest_framework import generics
from profiles.models import DummyUser
from trips.serializers import UserMinSerializer
from django.shortcuts import get_object_or_404

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


class UserDetail(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    '''
    '''
    queryset = DummyUser.objects.all()
    serializer_class = UserMinSerializer
    lookup_fields = ['pk', 'email']