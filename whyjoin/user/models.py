""" This module holds all models for the User Application """
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    """ Model represents the profile for the django user """

    # Each user can only have one user profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        """ Method creates profile at the same time as new user registers """
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        """ Method saves the profile created in the Profile model """
        instance.profile.save()

    def __str__(self):
        return f'{self.user.username} Profile'
