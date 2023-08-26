from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.db import IntegrityError
from django.urls import reverse

from .models import User

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            messages.error(request, 'Passwords must match.')
            return redirect('register')

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name 
            user.save()
        except IntegrityError:
            messages.error(request, 'Username already taken.')
            return redirect('register')
            
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('dashboard')
    else:
        return render(request, "accounts/register.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    else:
        return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect('dashboard')