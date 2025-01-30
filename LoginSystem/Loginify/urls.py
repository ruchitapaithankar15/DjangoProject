from django.urls import path
from .views import hello_world, login_view

urlpatterns = [
    path('', hello_world, name='hello'),  #URL for hello world
    path('login/', login_view, name='login'),  #URL for Login page
]