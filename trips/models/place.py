from datetime import date
from django.db import models
from django.db.models import Q
from .trip import Trip
import datetime


# Create your models here.
class Place(models.Model):
    CATEGORIES = (
        ("DINE", "DINING"), 
        ("SHOP", "SHOPPING"), 
        ("ATTR", "ATTRACTION")
        )

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255) 
    date = models.DateField(null = True, blank=True)
    time = models.TimeField(null = True, blank=True)
    note = models.TextField(blank = True)
    category = models.CharField(max_length = 4, choices = CATEGORIES)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name = 'places')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'trip'], name='Place can only be added to trip once'),
        ] 