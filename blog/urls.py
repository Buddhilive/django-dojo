from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView
)

urlpatterns = [
    path("", PostListView.as_view(), name="blog-home"),
    path("blog/<int:pk>/", PostDetailView.as_view(), name="blog-post-view"),
    path("blog/new/", PostCreateView.as_view(), name="blog-create-view")
]
