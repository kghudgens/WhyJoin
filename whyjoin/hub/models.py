""" This module holds all models for the Hub Application """

from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    """ Model represents the blog posts created by authorized users """
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    # Using the timezone library, can give the users post an automatic time
    created_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'Author : {self.author} Post : {self.title}'


class Comments(models.Model):
    """ Model represents the comments for its respective Post """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    email = models.EmailField()
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return f"Comment {self.name} on Post {self.post}"
