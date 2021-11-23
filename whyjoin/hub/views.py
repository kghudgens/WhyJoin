""" This module contains all of the views for the Hub app """
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Comments, Post


def index(request):
    """ This view serves as the home page for the Why Join App """
    return render(request, "hub/index.html")


def about(request):
    """ This view serves as the about page for the Why Join App """
    return render(request, "hub/about.html")


class PostListView(ListView):

    model = Post
    template_name = 'hub/post_list.html'


class PostDetailView(DetailView):

    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comments.objects.all()
        return context
