from django.db import models
from .trip import Trip

# Create your models here.
class Place(models.Model):
    CATEGORIES = (
        ("DINE", "DINING"), 
        ("SHOP", "SHOPPING"), 
        ("ATTR", "ATTRACTION")
        )

    name = models.CharField(max_length=255, unique = True)
    address = models.CharField(max_length=255, unique = True)
    # Required for trips, but not for proposals
    date = models.DateField(null = True)
    time = models.TimeField(null = True)
    note = models.TextField(blank = True)
    category = models.CharField(max_length = 4, choices = CATEGORIES)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name = 'places')