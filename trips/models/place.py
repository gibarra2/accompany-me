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

    # #Want to add constraint that place date must be between trip start_date and trip end_date
    # class Meta:
    #     constraints = [
    #         models.CheckConstraint(check=Q(date__gte= trip__start_date), name="date is after trip start date")
    #     ]
    # Also, want to add constraint that place can only be added to a trip once   
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'trip'], name='Place can only be added to trip once'),
        ] 