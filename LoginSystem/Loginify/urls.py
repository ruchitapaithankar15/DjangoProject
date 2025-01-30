from django.urls import path
from .views import hello_world, signup_view, login_view, success_view

urlpatterns = [
    path("", hello_world, name="hello"),
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("success/", success_view, name="success"),
]
