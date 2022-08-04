from rest_framework import serializers
from .models import Trip, Place
from profiles.models import DummyUser
from datetime import date

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
            'users'
            ]
        read_only_fields=['id']

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("End date must be after start date.")
        elif data['start_date'] < date.today():
            raise serializers.ValidationError("Start date must be after today's date.")
        return data

class TripUserSerializer(serializers.ModelSerializer):
    trip_id = serializers.IntegerField(source='id')
    class Meta:
        model = Trip
        fields = [
            'trip_id', 
            'users'
        ]

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
        read_only_fields=['id']
        extra_kwargs = {'trip': {'write_only': True}}
    

class TripPlaceSerializer(TripSerializer):
    places = serializers.SerializerMethodField()

    class Meta(TripSerializer.Meta):
        fields = TripSerializer.Meta.fields + ['places']

    def get_places(self, instance):
        places = instance.places.all().order_by('date', 'time')
        return PlaceSerializer(places, many=True).data

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

    def update(self, instance, validated_data):
        login_status = validated_data.get('is_logged_in', instance.is_logged_in)
        instance.is_logged_in = login_status
        return instance


class UserTripSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='id')
    trips = serializers.SerializerMethodField()
    class Meta:
        model = DummyUser
        fields = [
            'user_id',
            'trips',
            ]
        read_only_fields = ['user_id']
    
    def get_trips(self, instance):
        trips = instance.trips.all().order_by('start_date')
        return TripSerializer(trips, many=True).data
    
