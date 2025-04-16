from rest_framework import serializers
from .models import Trip, Place
from profiles.models import DummyUser, User
from django.contrib.auth.password_validation import validate_password
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
            'latitude',
            'longitude',
            'users'
            ]
        read_only_fields=['id', 'latitude', 'longitude']


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
    category = serializers.SerializerMethodField()
    class Meta:
        model = Place
        fields = '__all__'
        read_only_fields=['id', 'latitude', 'longitude']
        extra_kwargs = {'trip': {'write_only': True}}
    
    def get_category(self,obj):
        return obj.get_category_display()

class TripPlaceSerializer(TripSerializer):
    places = serializers.SerializerMethodField()

    class Meta(TripSerializer.Meta):
        fields = TripSerializer.Meta.fields + ['places']
        depth = 1

    def get_places(self, instance):
        places = instance.places.all().order_by('date', 'time')
        return PlaceSerializer(places, many=True).data
    

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id', 
            'first_name', 
            'last_name', 
            'email',
            'password'
        ]

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


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
    
