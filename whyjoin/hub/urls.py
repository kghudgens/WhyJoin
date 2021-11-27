""" The URL configuration for the Hub Application """
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("blog", views.PostListView.as_view(), name="post_list"),
    path("blog/<int:pk>", views.PostDetailView.as_view(), name="post_detail")
]
