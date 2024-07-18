from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm

def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Account created for {username}!')
            return redirect("login-page")
    else:
        form = UserRegistrationForm()
    return render(request, "users/register.html", { "form": form })

def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')

@login_required
def profile_view(request):
    user_form = UserUpdateForm()
    profile_form = ProfileUpdateForm()
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    
    return render(request, 'users/profile.html', context)
