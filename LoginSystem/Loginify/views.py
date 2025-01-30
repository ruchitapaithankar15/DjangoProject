from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import UserDetails
from django.http import HttpResponse, JsonResponse
import json

from django.views.decorators.csrf import csrf_exempt


def hello_world(request):
    return HttpResponse("Hello, world!")

@csrf_exempt
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

# Get all users' details
def get_all_users(request):
    users = list(UserDetails.objects.values()) 
    return JsonResponse({"users": users}, safe=False)

# Get a single user by email
def get_user_by_email(request, email):
    user = get_object_or_404(UserDetails, email=email)
    return JsonResponse({
        "username": user.username,
        "email": user.email,
        "password": user.password 
    })


def update_user(request, email):
    if request.method == "POST":
        try:
            data = json.loads(request.body) 
            user = get_object_or_404(UserDetails, email=email)
            user.username = data.get("username", user.username)
            user.password = data.get("password", user.password)
            user.save()
            return JsonResponse({"message": "User updated successfully"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)


def delete_user(request, email):
    if request.method == "DELETE":
        user = get_object_or_404(UserDetails, email=email)
        user.delete()
        return JsonResponse({"message": "User deleted successfully"})
    return JsonResponse({"error": "Invalid request method"}, status=405)
