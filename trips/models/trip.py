from django.conf import settings
from django.db import models

class Trip(models.Model):
    city = models.CharField(max_length=126)
    country = models.CharField(max_length=126)
    start_date = models.DateField()
    end_date = models.DateField()
    is_proposal = models.BooleanField(default=False)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)