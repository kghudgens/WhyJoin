""" This module contains all of the views for the Hub app """
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Comments, Post


def index(request):
    """ This view serves as the home page for the Why Join App """

    blog_post = Post.objects.all()[:3]

    context = {"blog_post": blog_post}
    return render(request, "hub/index.html", context)


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


class CreatePostView(LoginRequiredMixin, CreateView):
    """
    Class based view that grants a logged in user the permissions to create a new post.
    """
    model = Post
    fields = ['title', 'text', 'images']

    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeletePostView(LoginRequiredMixin, DeleteView):
    """
    Class based view that allows the author of a particular post delete it if 
    they choose to.
    """
    model = Post
    success_url = reverse_lazy('post_list')

    def test_func(self):
        self.object = self.get_object()
        return self.request.user == self.object.author


class UpdatePostView(LoginRequiredMixin, UpdateView):
    """
    Class based view that gives the user that created the post the ability to 
    update their previously created blog post object.
    """

    model = Post
    fields = ['title', 'text', 'images']
    template_suffix = '_update_form'
