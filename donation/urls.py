
from tokenize import Number
from xmlrpc.client import Boolean
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("categories", views.categories, name="categories"),
    path("<int:listing_id>", views.listing, name="listing"),
    path("listings", views.listings, name="listings"),
    path("add_new_listing", views.add_new_listing, name="add_new_listing"),
    path("profile_page/<int:user_id>", views.profile_page, name="profile_page"),
    path("claim_offer/<int:listing_id>", views.claim_offer, name="claim_offer"),
    path("stripe_checkout/<str:session_mode>/<int:price_id>", views.stripe_checkout, name="stripe_checkout"),
    path("success", views.success, name="success"),
    path("cancel", views.cancel, name="cancel"),
    path("donation_checkout", views.donation_checkout, name="donation_checkout")
]