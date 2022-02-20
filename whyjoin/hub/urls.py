""" The URL configuration for the Hub Application """
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("blog", views.PostListView.as_view(), name="post_list"),
    path("blog/<int:pk>", views.PostDetailView.as_view(), name="post_detail"),
    path("blog/write", views.CreatePostView.as_view(), name="write_post"),
    path("blog/<int:pk>/delete/", views.DeletePostView.as_view(), name="delete_post"),
    path("blog/<int:pk>/update/", views.UpdatePostView.as_view(), name="update_post")
]
