from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)


class Profile(models.Model):
    is_logged_in = models.BooleanField(default=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class DummyUser(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    is_logged_in = models.BooleanField(default=False)