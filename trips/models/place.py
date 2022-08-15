from datetime import date
from django.db import models
from django.db.models import Q
from .trip import Trip
from trips.geocoding import address_geocoding


# Create your models here.
class Place(models.Model):
    CATEGORIES = (
        ("DINE", "Dining"), 
        ("SHOP", "Shopping"), 
        ("ATTR", "Attraction")
        )

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255) 
    date = models.DateField(null = True, blank=True)
    time = models.TimeField(null = True, blank=True)
    note = models.TextField(blank = True)
    category = models.CharField(max_length = 4, choices = CATEGORIES)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name = 'places')
    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'trip'], name='Place can only be added to trip once'),
        ] 

    def save(self, *args, **kwargs):
        if not self.latitude or not self.longitude:
            coord = address_geocoding(self.address)
            self.latitude = coord["lat"]
            self.longitude = coord["lng"]
        
        super(Place, self).save(*args, **kwargs)
