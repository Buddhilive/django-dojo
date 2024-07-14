from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register_view, name="register-page"),
    path("login", auth_views.LoginView.as_view(template_name="users/login.html"), name="login-page"),
    path("logout", auth_views.LogoutView.as_view(), name="logout-page")
]
