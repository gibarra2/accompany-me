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
            'is_proposal'
            ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DummyUser
        fields = [
            'id', 
            'first_name', 
            'last_name', 
            'email',
            'is_logged_in'
        ]

        extra_kwargs = {'email': {'write_only': True}}

    def update(self, instance, validated_data):
        login_status = validated_data.get('is_logged_in', instance.is_logged_in)
        instance.is_logged_in = login_status
        return instance


class UserTripSerializer(serializers.ModelSerializer):
    trips = TripSerializer(many=True)
    class Meta:
        model = DummyUser
        fields = [
            'id',
            'trips',
            ]
        read_only_fields = ['id']
