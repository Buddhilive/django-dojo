from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register_view, name="register-page"),
    path("login", auth_views.LoginView.as_view(template_name="users/login.html"), name="login-page"),
    path("logout", views.logout_view, name="logout-page"),
    path("profile", views.profile_view, name="profile-page")
]
