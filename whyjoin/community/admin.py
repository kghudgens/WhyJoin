""" This module registers selected models in the admin site for model manipulation """

from django.contrib import admin
from .models import CommunityBranch, CommunityForums
# Register your models here.

admin.site.register(CommunityForums)
admin.site.register(CommunityBranch)
