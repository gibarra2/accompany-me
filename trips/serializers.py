from wsgiref import validate
from rest_framework import serializers
from .models import Trip, Place
# from django.conf import settings
from profiles.models import DummyUser

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = [
            'id',
            'city', 
            'country', 
            'start_date', 
            'end_date', 
            'is_proposal',
            ]

        # def create(self, validated_data):
        #     trips_data = validated_data.pop('trips')
        #     user = DummyUser.create(**validated_data)
        #     for trip_data in trips_data:
        #         Trip.objects.create(user=user, **trip_data)
        #     return user
class UserMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = DummyUser
        fields = [
            'id', 
            'first_name', 
            'last_name', 
            'email', 
            'is_logged_in'
        ]

class UserTripSerializer(serializers.ModelSerializer):
    trips = TripSerializer(many=True)
    class Meta:
        model = DummyUser
        fields = [
            'id',
            'trips',
            ]
        read_only_fields = ['id']

    # def create(self, instance,  validated_data):
    #     trips_data = validated_data.pop('trips')
    #     print(validated_data)
    #     user = instance
    #     for trip_data in trips_data:
    #         Trip.objects.update(user=user, **trip_data)
    #     return user
    
    # def update(self, instance, validated_data):
    #     trips_data = validated_data.pop('trips')
    #     print(validated_data)
    #     user = instance
    #     for trip_data in trips_data:
    #         Trip.objects.update(users=user, **trip_data)
    #     return user

# class PlaceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Place
#         fields = []

