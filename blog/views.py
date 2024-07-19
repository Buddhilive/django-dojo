from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
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
    
class PostDetailView(DetailView):
    model = BlogPost
    
class PostCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    