from django.conf import settings
from django.db import models
from profiles.models import DummyUser
from trips.geocoding import city_geocoding

class Trip(models.Model):
    city = models.CharField(max_length=126)
    country = models.CharField(max_length=126)
    start_date = models.DateField()
    end_date = models.DateField()
    is_proposal = models.BooleanField(default=False)
    users = models.ManyToManyField(DummyUser, blank=True, related_name="trips")
    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True)

    def save(self, *args, **kwargs):
        if not self.latitude or not self.longitude:
            coord = city_geocoding(self.city, self.country)
            self.latitude = coord["lat"]
            self.longitude = coord["lng"]
        
        super(Trip, self).save(*args, **kwargs)
