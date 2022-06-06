from django.contrib import admin

from .models import User, Category, WhoPays, ListingOffer, Gender, Price, Country

# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(WhoPays)
admin.site.register(ListingOffer)
admin.site.register(Gender)
admin.site.register(Price)
admin.site.register(Country)