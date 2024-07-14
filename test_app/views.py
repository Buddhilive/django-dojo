from django.shortcuts import render
from .models import TodoItem

# Create your views here.
def home(request):
    return render(request, "test_app/index.html")

def todos(request):
    todo_items = TodoItem.objects.all()
    return render(request, "test_app/todo.html", { "todos": todo_items })