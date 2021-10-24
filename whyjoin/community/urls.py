""" The URL configuration for the Community Application """
from django.urls import path

from . import views

urlpatterns = [
    path("", views.community, name="community")
]
