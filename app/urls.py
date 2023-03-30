from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .forms import *

urlpatterns = [
    path("",views.home, name="home"),

    path("registration/",
        views.RegistrationView.as_view(),
        name="registration",
    ),

    path("accounts/login/",
        auth_views.LoginView.as_view(
            template_name="login.html", authentication_form=LoginForm
        ),
        name="login",
    ),

    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),

    path("stockpicker/",views.stock_picker, name="stockpicker"),
    path("stocktracker/",views.stock_tracker, name="stocktracker"),
]
