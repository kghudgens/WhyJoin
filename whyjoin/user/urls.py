""" The URL configuration for the User Application """

from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:user_id>', views.profile, name='profile'),
    path("register/", views.register_request, name='register')
]
