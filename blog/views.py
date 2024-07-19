from django.shortcuts import render
from django.views.generic import ListView
from .models import BlogPost

def view_home(request):
    context = {
        'blog_posts': BlogPost.objects.all()
    }
    return render(request, "blog/index.html", context)

class PostListView(ListView):
    model = BlogPost
    # <app>/<model>_<viewtype>.html
    template_name = 'blog/index.html'
    context_object_name = 'blog_posts'
    ordering = ['-date_posted']