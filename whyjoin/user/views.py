""" This module holds all views for the User Application"""
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import NewUser
from .models import Profile


class Login(LoginView):
    """ 
    Class represents the view that logs in the user. Inherits from Django Generic LoginView and is provided the form to log in from django.
    """
    template_name = 'user/login.html'


class Logout(LogoutView):
    """
    Class represents the view that logs the user out of the application. 
    Inherits from the Django Generic LogoutView and is provided the form from Django.
    """
    template_name = 'user/logout.html'


def register_request(request):
    """
    Method that passes the registration form to its appropriate template with a
    POST method to save to the PostgreSQL DB.
    """
    if request.method == "POST":
        form = NewUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect('index')
    else:
        form = NewUser()
    return render(request, "user/register.html", {"form": form})


@login_required
def profile(request, user_id):
    """
    Method requests the logged in user and displays it to the template for the 
    frontend.
    """
    profile = User.objects.get(id=user_id)
    context = {"profile": profile}
    return render(request, "user/profile.html", context)
