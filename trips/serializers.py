from wsgiref import validate
from rest_framework import serializers
from .models import Trip, Place
# from django.conf import settings
from profiles.models import DummyUser

class TripSerializer(serializers.ModelSerializer):
    # users = UserSerializer(many=True, read_only=True)
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
            'places',
            # Need to add places as well
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

class UserDetailSerializer(serializers.ModelSerializer):
    trips = TripSerializer(many=True)
    class Meta:
        model = DummyUser
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'is_logged_in', 
            'trips',
            ]
        extra_kwargs = {'is_logged_in': {'write_only': True}}

    def create(self, validated_data):
        trips_data = validated_data.pop('trips')
        user = DummyUser.create(**validated_data)
        for trip_data in trips_data:
            Trip.objects.create(user=user, **trip_data)
        return user

    def update(self, instance, validated_data):
        pass
        


# class PlaceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Place
#         fields = []

