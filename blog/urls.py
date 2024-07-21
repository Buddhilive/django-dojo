from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path("", PostListView.as_view(), name="blog-home"),
    path("blog/<int:pk>/", PostDetailView.as_view(), name="blog-post-view"),
    path("blog/new/", PostCreateView.as_view(), name="blog-create-view"),
    path("blog/<int:pk>/edit/", PostUpdateView.as_view(), name="blog-update-view"),
    path("blog/<int:pk>/delete/", PostDeleteView.as_view(), name="blog-delete-view"),
]
