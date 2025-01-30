from django.shortcuts import render

from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("Hello, world!")

def login_view(request):
    return render(request, 'Loginify/login.html')
