from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.db import IntegrityError
from django.conf import settings
from datetime import datetime

from .models import User, Category, ListingOffer, Price, Country, Gender, Transaction
from .forms import NewListingForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

from django.views.decorators.csrf import csrf_exempt
import stripe
from django.shortcuts import render

stripe.api_key = settings.STRIPE_PRIVATE_KEY

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
        location_country = request.POST["country_name"]
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
        return render(request, "donation/register.html", {
            'countries': Country.objects.all()
        })

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
            "form": NewListingForm(initial={
                "gender": Gender.objects.get(id=1)
            })
        })

@login_required
def profile_page(request, user_id):
    user = User.objects.get(pk=user_id)
    donated_listings = ListingOffer.objects.filter(owner = user)
    received_listings = ListingOffer.objects.filter(recipient = user)
    return render(request, "donation/profile_page.html", {
        "user": user,
        "donated_listings_count": donated_listings.count(),
        "received_listings_count": received_listings.count(),
    })

#success view
def success(request):
    amount = int(request.GET.get('amount'))/100
    transaction = Transaction()
    transaction.amount = amount
    transaction.save()
    pay_shipping()
    return render(request,'donation/success.html')
    
#cancel view
def cancel(request):
    return render(request,'donation/cancel.html')

#checkout donation
@csrf_exempt
def stripe_checkout(request, session_mode, price_id):
    YOUR_DOMAIN = 'http://127.0.0.1:8000'
    if price_id == 0:
        price = int(request.POST["value_price"]) * 100
    else:
        price_info = Price.objects.get(pk=price_id)
        price = price_info.price
    checkout_mode = 'payment'
    payment_item = {
        'price_data': {
            'currency': 'usd',
            'product_data': {
                'name': 'We appreciate your donation',
            },
            'unit_amount': price,
        },
        'quantity': 1
    }
    if (session_mode == 'subscription'):
        payment_item['price_data']['recurring'] = {
            'interval': 'month'
        }
        payment_item['price_data']['product_data']['name'] = 'monthly donations'

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items = [payment_item],
        mode = session_mode,
        success_url = YOUR_DOMAIN + '/success?amount=' + str(price),
        cancel_url= YOUR_DOMAIN + '/cancel',
    )
    return HttpResponseRedirect(session.url)


# def requiring_payment(price_id):
#     YOUR_DOMAIN = 'http://127.0.0.1:8000'
#     price_info = Price.objects.get(pk=price_id)
#     price = price_info.price
#     session = stripe.checkout.Session.create(
#         payment_method_types=['card'],
#         line_items = [{
#         'price_data': {
#             'currency': 'usd',
#             'product_data': {
#             'name': 'We appreciate your monthly donation',
#             },
#             'unit_amount': price,
#         },
#         'quantity': 1,
#         }],
#         mode = 'subscription',
#         success_url = YOUR_DOMAIN + '/success',
#         cancel_url= YOUR_DOMAIN + '/cancel',
#     )
#     return HttpResponseRedirect(session.url)

def donation_checkout(request):
    prices = Price.objects.all()
    countries = Country.objects.order_by("name").all()
    return render(request, 'donation/donation_checkout.html', {
        'countries': countries,
        'prices': prices
    })

#success view
def about_us(request):
    return render(request,'donation/about_us.html', {
        'total_shipping_cost': total_shipping_cost(),
        'total_received_amount': total_received_amount()
    })

# total cost for pending items for shipping 
def total_shipping_cost():
    claimed_listings = ListingOffer.objects.filter(status = "pending", recipient__isnull=False)
    shipping_cost = 0
    for listing in claimed_listings:
        shipping_cost += listing.shipping_cost
    return shipping_cost

#total received amount
def total_received_amount():
    transactions = Transaction.objects.all()
    amount = 0
    for transaction in transactions:
        if transaction.amount > 0:
            amount += transaction.amount
    return amount

#try to pay for shipping
def pay_shipping():
    print("entered the pay shipping")
    funds_available = get_funds_available()
    print(funds_available)
    claimed_listings = ListingOffer.objects.filter(status = "pending", recipient__isnull=False)
    for listing in claimed_listings:
        print(listing.title)
        print(listing.shipping_cost)
        if funds_available >= listing.shipping_cost:
            transaction = Transaction()
            transaction.amount = -listing.shipping_cost
            transaction.save()
            print(f"after save {funds_available}")
            funds_available -= listing.shipping_cost
            print(f"after deduction {funds_available}")
            listing.status = "claimed" 
            listing.save() 
    print("end the pay shipping")      
    return funds_available

#get funds available
def get_funds_available():
    transactions = Transaction.objects.all()
    amount_available = 0
    for transaction in transactions:
        amount_available += transaction.amount
    return amount_available

#claim donation
@login_required
def claim_offer(request, listing_id, is_paying):
    print(f"first {is_paying}")
    if request.method == "POST":
        listing = ListingOffer.objects.get(pk=listing_id)
        listing.claimed_time = datetime.now()
        # if "sponsor" in request.POST:
        if is_paying.lower() != "true":
            listing.status = "pending"
            print(f"{listing.title}  pending status {listing.status}")
        else:
            listing.status = "claimed"
            print(f"{listing.title} claimed status {listing.status}")
        recipient = request.user
        listing.recipient = recipient
        listing.save()
        print(f"{listing.title}, {listing.status}")
        pay_shipping()
        return render(request, "donation/listing.html", {
            "listing": listing,
        })
    else:
        return HttpResponseRedirect(reverse("listing", args=(listing_id,)))

