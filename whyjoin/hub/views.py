""" This module contains all of the views for the Hub app """
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Comments, Post


def index(request):
    """ This view serves as the home page for the Why Join App """
    return render(request, "hub/index.html")


def about(request):
    """ This view serves as the about page for the Why Join App """
    return render(request, "hub/about.html")


class PostListView(ListView):
    """
    Class based view that queries the Post model for hub blog objects. The view 
    displays all objects on the template.
    """
    model = Post
    template_name = 'hub/post_list.html'


class PostDetailView(DetailView):
    """
    Class based view that displays the particular post object being choosen by 
    the user. The view also queries the Comments model to display along side 
    the Post it is assigned.
    """
    model = Post
    template_name = 'hub/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comments.objects.all()
        return context


class CreatePostView(CreateView):

    model = Post
    fields = ['title', 'text']
