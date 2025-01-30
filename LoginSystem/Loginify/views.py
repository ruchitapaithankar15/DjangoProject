from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserDetails
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, world!")

def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        # Check if email already exists
        if UserDetails.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("signup")

        # Create new user
        user = UserDetails(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Signup successful! Please log in.")
        return redirect("login")

    return render(request, "Loginify/signup.html")

def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        # Authenticate user
        user = UserDetails.objects.filter(email=email, password=password).first()

        if user:
            messages.success(request, "Login successful! Welcome, " + user.username)
            return redirect("success")
        else:
            messages.error(request, "Invalid email or password.")
            return redirect("login")

    return render(request, "Loginify/login.html")

def success_view(request):
    return render(request, "Loginify/success.html")
