""" This module holds all models for the User Application """
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    """ 
    Model represents the profile for the django user. Adding on to the 
    information provided by the django user model 
    """

    # Each user can only have one user profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(blank=True, default="")
    title = models.TextField(blank=True, default="")
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        return f'{self.user.username} Profile'
