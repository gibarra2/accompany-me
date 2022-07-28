from rest_framework import serializers
from .models import Trip, Place
# from django.conf import settings
from profiles.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            # 'is_logged_in'
            ]

class TripSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Trip
        fields = [
            'id',
            'city', 
            'country', 
            'start_date', 
            'end_date', 
            'is_proposal', 
            'users', 
            # Need to add places as well
            ]
    

# class PlaceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Place
#         fields = []

