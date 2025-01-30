from django.urls import path
from .views import hello_world, signup_view, login_view, success_view, get_all_users, get_user_by_email, update_user, delete_user

urlpatterns = [
    path("", hello_world, name="hello"),
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("success/", success_view, name="success"),

    # CRUD Operations
    path("users/", get_all_users, name="get_all_users"),
    path("users/<str:email>/", get_user_by_email, name="get_user_by_email"),
    path("users/update/<str:email>/", update_user, name="update_user"),
    path("users/delete/<str:email>/", delete_user, name="delete_user"),
]