from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .forms import CustomUserCreationForm,CustomAuthenticationForm
from django import forms

def index(request):
    return render(request,'users/index.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('/')  # Redirect to the homepage
    else:
        form = CustomUserCreationForm()  # Use the custom form

    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            # Get the user object from the form
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                next_url = request.POST.get('next', '')
                return redirect(next_url if next_url else '/')  # Redirect after successful login
    else:
        form = CustomAuthenticationForm()

    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    if request.method == "POST": 
        logout(request) 
        return redirect("/")

def about(request):
    return render(request,'users/aboutus.html')

def contact(request):  
    return render(request,'users/contact.html')