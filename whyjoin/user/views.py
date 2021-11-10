""" This module holds all views for the User Application"""
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView


class Login(LoginView):
    template_name = 'user/login.html'
