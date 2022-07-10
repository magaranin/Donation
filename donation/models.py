from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    location_country = models.CharField( max_length=30, blank=True)
    location_city = models.CharField( max_length=30, blank=True)
    profile_image = models.ImageField(upload_to='profile_images', default="images/default.jpg")
    def __str__(self):
        if len(super().get_full_name()) > 0:
            return super().get_full_name()
        else:
            return super().get_username()

class Category(models.Model):
    name = models.CharField(max_length=30)
    class Meta: 
        verbose_name_plural = "Categories"    
    def __str__(self):
        return f"{self.name}"

class Gender(models.Model):
    name = models.CharField(max_length=30, default="Girl") 
    def __str__(self):
        return f"{self.name}"


class WhoPays(models.Model):
    name = models.CharField(max_length = 200, default="Willing to pay for delivery")
    class Meta: 
        verbose_name_plural = "Who Pays"  
    def __str__(self):
        return f"{self.name}"

class ListingOffer(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(null=True, max_length=1000)
    post_date = models.DateTimeField(auto_now=True)
    images = models.FileField(upload_to='images', blank=True, default="images/listing_default.jpg")
    categories = models.ManyToManyField(Category)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="owner")
    who_pays = models.ForeignKey(WhoPays, on_delete=models.CASCADE)
    delivery_cost = models.DecimalField(max_digits=5, decimal_places=2)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="recipient")
    claimed_time = models.DateTimeField(null=True)
    def __str__(self):
        return f"{self.title}"

class Price(models.Model):
    price = models.IntegerField(default=0)  # cents
	
    def get_display_price(self):
        return "{0:.0f}".format(self.price / 100)
    def __str__(self):
        return f"{self.price}"

class Country(models.Model):
    name = models.CharField(max_length=30)
    class Meta: 
        verbose_name_plural = "Countries"  
    def __str__(self):
        return f"{self.name}"