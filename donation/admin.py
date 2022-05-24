from django.contrib import admin

from .models import User, Category, WhoPays, ListingOffer, Gender

# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(WhoPays)
admin.site.register(ListingOffer)
admin.site.register(Gender)