from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import UserDetails

def hello_world(request):
    return HttpResponse("Hello, world!")

@csrf_exempt
def signup_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")

            # Create user only if email does not exist
            user, created = UserDetails.objects.get_or_create(email=email, defaults={"username": username, "password": password})

            if not created:
                return JsonResponse({"error": "Email already registered"}, status=400)

            return JsonResponse({"message": "Signup successful", "username": user.username, "email": user.email}, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email")
            password = data.get("password")

            user = UserDetails.objects.filter(email=email, password=password).first()

            if user:
                return JsonResponse({"message": f"Login successful! Welcome, {user.username}"}, status=200)
            else:
                return JsonResponse({"error": "Invalid email or password"}, status=401)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)

def success_view(request):
    return render(request, "Loginify/success.html")

@csrf_exempt
def get_all_users(request):
    if request.method == "GET":
        users = list(UserDetails.objects.values())
        return JsonResponse({"users": users}, safe=False)
    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def get_user_by_email(request, email):
    if request.method == "GET":
        user = get_object_or_404(UserDetails, email=email)
        return JsonResponse({"username": user.username, "email": user.email, "password": user.password})
    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def update_user(request, email):
    if request.method == "PUT":
        try:
            user = get_object_or_404(UserDetails, email=email)
            data = json.loads(request.body)

            user.username = data.get("username", user.username)
            user.password = data.get("password", user.password)
            user.save()

            return JsonResponse({"message": "User updated successfully", "updated_user": {"username": user.username, "email": user.email}}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def delete_user(request, email):
    if request.method == "DELETE":
        try:
            user = get_object_or_404(UserDetails, email=email)
            user.delete()
            return JsonResponse({"message": "User deleted successfully"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)
