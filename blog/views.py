from django.shortcuts import render

posts = [
    {
        'author': 'Buddhi Kavindra',
        'title': 'Welcome',
        'content': 'Lorem ipsum...',
        'date_posted': 'May 13, 2024'
    },
    {
        'author': 'John Doe',
        'title': 'Getting Started',
        'content': 'Lorem ipsum...',
        'date_posted': 'June 13, 2024'
    }
]

def view_home(request):
    context = {
        'blog_posts': posts
    }
    return render(request, "blog/index.html", context)