from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.db import IntegrityError
from django.conf import settings
from datetime import datetime

from .models import User, Category, ListingOffer
from .forms import NewListingForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

from django.views.decorators.csrf import csrf_exempt
import stripe
from django.shortcuts import render

stripe.api_key = settings.STRIPE_PRIVATE_KEY
YOUR_DOMAIN = 'http://127.0.0.1:8000'

def index(request):
    listings = None
    if request.user.is_authenticated:
        listings = ListingOffer.objects.filter(owner = request.user)
    return render(request, "donation/index.html", {
        "listings": listings
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "donation/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "donation/login.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        profile_image = request.FILES.get("profile_image")
        location_country = request.POST["location_country"]
        location_city = request.POST["location_city"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "donation/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(
                username, 
                email = email, 
                password = password, 
                first_name = first_name, 
                last_name = last_name, 
                profile_image = profile_image,
                location_country = location_country, 
                location_city = location_city)
            user.save()
        except IntegrityError:
            return render(request, "donation/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "donation/register.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def categories(request):
    return render(request,"donation/categories.html", {
        "categories": Category.objects.all()
    })


def listing(request, listing_id):
    listing = ListingOffer.objects.get(pk=listing_id)
    return render(request, "donation/listing.html", {
        "listing": listing
    })


def listings(request):
    select_cat=int(request.GET.get('category_id', -1))
    donation= request.GET.get('show', '')
    if select_cat >= 1:
        listings = ListingOffer.objects.filter(categories__id__contains = select_cat)
    elif donation == "claimed":
        listings = ListingOffer.objects.filter(recipient__isnull=False)
    else:
        listings = ListingOffer.objects.filter(recipient__isnull=True)
    return render(request, "donation/listings.html", {
        "listings": listings
    })

@login_required
def add_new_listing(request):
    if request.method == "POST":
        form = NewListingForm(request.POST, request.FILES)
        if form.is_valid():
            new_listing_offer = form.save(commit=False)
            new_listing_offer.owner = request.user
            new_listing_offer.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse("listing", kwargs={'listing_id': new_listing_offer.id}))
    else:
        return render(request, "donation/add_new_listing.html", {
            "form": NewListingForm()
        })

@login_required
def profile_page(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, "donation/profile_page.html", {
        "user": user,
    })

@login_required
def claim_offer(request, listing_id):
    if request.method =="POST":
        listing = ListingOffer.objects.get(pk=listing_id)
        listing.claimed_time = datetime.now()
        recipient = request.user
        listing.recipient = recipient
        listing.save()
        return render(request, "donation/listing.html", {
            "listing": listing,
        })
    else:
        return HttpResponseRedirect(reverse("listing", args=(listing_id,)))

#success view
def success(request):
    return render(request,'donation/success.html')
    
#cancel view
def cancel(request):
    return render(request,'donation/cancel.html')

#checkout donation
@csrf_exempt
def donation_checkout(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items = [{
        'price_data': {
            'currency': 'usd',
            'product_data': {
            'name': ':)',
            },
            'unit_amount': 5000,
        },
        'quantity': 1,
        }],
        mode='payment',
        success_url = YOUR_DOMAIN + '/success',
        cancel_url= YOUR_DOMAIN + '/cancel',
    )
    return HttpResponseRedirect(session.url)