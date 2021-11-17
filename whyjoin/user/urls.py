""" The URL configuration for the User Application """

from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:user.id>', views.profile, name='profile')
]
