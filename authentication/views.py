from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
# from rest_framework.decorators import api_view

# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['pass1']
        
        try:
            user = User.objects.create_user(username, email, password1)
            user.username = username
            user.email = email
            user.save()

            messages.success(request, "Account has been succesfully created")
            return redirect("signin")

        except IntegrityError:
            messages.error(request, "Username and email must be unique. Try again")

    return render(request, "authentication/signup.html")

def signin(request):
    
    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST["pass1"]

        user = authenticate(username=username, \
                                password=pass1) # returns None is usernames don't match

        if user is not None:
            login(request, user)
            return render(request, "authentication/index.html")
        else:
            messages.error(request, "Incorrect credentials")
            return redirect("home")

    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("home")

# @api_view(['GET'])
def read_users(request):

    if request.method == "GET":
        users = User.objects.all()
        print("Users:")
        for user in users:
            print(f"Username: {user.username}, Email: {user.email}")
        return render(request, "authentication/read_users.html", {"users":users})

def get_user(request, username):
    
    if request.method == "GET":
        user = User.objects.get(username=username)
        print(f"User {username} details found: {user.username}, {user.email}")
    return render(request, "authentication/get_user.html", {'user':user})