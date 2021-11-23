""" This module contains all of the views for the Hub app """
from django.shortcuts import render
from django.views.generic import ListView

from .models import Post


def index(request):
    """ This view serves as the home page for the Why Join App """
    return render(request, "hub/index.html")


def about(request):
    """ This view serves as the about page for the Why Join App """
    return render(request, "hub/about.html")


class PostListView(ListView):

    model = Post
