""" This module registers the created models with the admin site """
from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
