from django.shortcuts import render
from .models import TodoItem

# Create your views here.
def home(request):
    return render(request, "index.html")

def todos(request):
    todo_items = TodoItem.objects.all()
    return render(request, "todo.html", { "todos": todo_items })