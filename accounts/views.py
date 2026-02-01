from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':# if form is submitted
        form = RegisterForm(request.POST)
        if form.is_valid():# built-in form validation, checks if data is correct or not
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration is Successful.')# success message after registration
            return redirect('slinks:home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})# if GET request, render empty form

def login_view(request):
    return render(request, 'accounts/login.html')

def logout_view(request):
    return render(request, 'accounts/logout.html')
