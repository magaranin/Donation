from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db import IntegrityError

from .models import User

# Create your views here.

def index(request):
    return render(request, "donation/index.html")

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