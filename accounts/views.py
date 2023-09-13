from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.db import IntegrityError
from django.urls import reverse

from accounts.models import User, Profile
from tickets.models import Ticket

from accounts.forms import UpdateProfileForm

def dashboard(request):
    if request.user.is_authenticated:
        if Ticket.objects.filter(customer=request.user.id).exists():
            user_tickets = Ticket.objects.filter(customer=request.user.id).order_by('-created_date')
            context = {
                'tickets': user_tickets
            }
            return render(request, 'accounts/dashboard.html', context)
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

@login_required
def profile_view(request):
    user_id = request.user.id
    user_profile = Profile.objects.get(user_id=user_id)
    user_tickets = Ticket.objects.filter(customer=user_id).order_by('-created_date')
    context = {
        'user_profile': user_profile,
        'tickets': user_tickets
        }
    return render(request, "accounts/profile.html", context)

@login_required
def update_profile(request):
    user_id = request.user.id 
    user_profile = get_object_or_404(Profile, pk=user_id)
    
    if request.method == 'POST':
        form = UpdateProfileForm(
            request.POST, request.FILES, instance=request.user.profile)
        
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('profile')
    else:
        form = UpdateProfileForm(instance=request.user.profile)
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/profile.html', context)
