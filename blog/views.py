from django.shortcuts import render
from .models import BlogPost

def view_home(request):
    context = {
        'blog_posts': BlogPost.objects.all()
    }
    return render(request, "blog/index.html", context)