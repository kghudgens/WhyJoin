""" This module registers the created models with the admin site """

from django.contrib import admin
from .models import Comments, Post

# Registered the models on the admin page
admin.site.register(Post)
admin.site.register(Comments)
