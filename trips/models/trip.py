from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
    city = models.CharField(max_length=126)
    country = models.CharField(max_length=126)
    start_date = models.DateField()
    end_date = models.DateField()
    is_proposal = models.BooleanField(default=False)
    users = models.ManyToManyField(User)