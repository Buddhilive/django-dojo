from django.shortcuts import render
from .models import BlogPosts

def view_home(request):
    context = {
        'blog_posts': BlogPosts.objects.all()
    }
    return render(request, "blog/index.html", context)