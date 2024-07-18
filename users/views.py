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
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account haas been updated')
            return redirect("profile-page")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    
    return render(request, 'users/profile.html', context)
