from django.contrib import admin

from .models import User, Category, DeliveryPayment, ListingOffer, Gender

# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(DeliveryPayment)
admin.site.register(ListingOffer)
admin.site.register(Gender)