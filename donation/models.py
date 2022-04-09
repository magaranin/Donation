from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass
    location_country = models.CharField( max_length=30, blank=True)
    location_city = models.CharField( max_length=30, blank=True)

    def __str__(self):
        return f"{self.username}"