from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

from krishiapp.models import UserProfile

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')


def signup(request):
    if request.method == 'POST':
        try:
            user = User.objects.create(username=request.POST.get('username'),
                                       email=request.POST.get('email'),
                                       password=make_password(request.POST.get('password')),
                                       is_superuser=0, is_active=1)
            UserProfile.objects.create(user=user, address=request.POST.get('address'),
                                       first_name=request.POST.get('first_name'),
                                       last_name=request.POST.get('last_name'),
                                       contact=request.POST.get('contact'))
            messages.success(request, 'User created successfully.')
        except Exception as error:
            print(error)
            messages.error(request, 'User creation failed. Please try again.')
    return render(request, 'signup.html')


def login_user(request):
    if request.method == 'POST':
        try:
            user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
            if user:
                login(request, user)
                messages.success(request, 'Login Successful.')
                return redirect('homepage')
            else:
                messages.error(request, 'Please enter correct username and password.')
        except Exception as error:
            messages.error(request, 'Something went wrong. Please try again.')

    return render(request, 'login.html')


def about(request):
    return render(request, 'about.html')
