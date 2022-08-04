from functools import partial
from rest_framework.generics import RetrieveUpdateDestroyAPIView
# from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from trips.serializers import PlaceSerializer
from django.shortcuts import get_object_or_404
from trips.models import Place
from rest_framework.decorators import api_view

# Create routes to edit, and delete individual places
class PlaceDetail(RetrieveUpdateDestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    http_method_names =  ['get', 'patch', 'delete']


