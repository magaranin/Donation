from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    location_country = models.CharField( max_length=30, blank=True)
    location_city = models.CharField( max_length=30, blank=True)
    profile_image = models.ImageField(upload_to='profile_images', blank=True, default=None, null=True)
    

    def __str__(self):
        return super().get_full_name()

class Category(models.Model):
    name = models.CharField(max_length=30)
    class Meta: 
        verbose_name_plural = "Categories"    
    def __str__(self):
        return f"{self.name}"

class Gender(models.Model):
    name = models.CharField(max_length=30) 
    def __str__(self):
        return f"{self.name}"


class WhoPays(models.Model):
    name = models.CharField(max_length = 200)
    class Meta: 
        verbose_name_plural = "Who Pays"  
    def __str__(self):
        return f"{self.name}"

class ListingOffer(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(null=True, max_length=1000)
    post_date = models.DateTimeField(auto_now=True)
    images = models.FileField(upload_to='listing_images', blank=True, default=None)
    categories = models.ManyToManyField(Category)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="owner")
    who_pays = models.ForeignKey(WhoPays, on_delete=models.CASCADE)
    delivery_cost = models.DecimalField(max_digits=5, decimal_places=2)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="recipient")
    claimed_time = models.DateTimeField(null=True)
