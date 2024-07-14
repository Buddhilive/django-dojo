from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view_home(request):
    return HttpResponse("<h1>Welcome to Blog<h2>")