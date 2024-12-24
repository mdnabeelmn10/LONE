from django.shortcuts import render

def index(request):
    return render(request,'users/index.html')

def login_view(request):
    return render(request,'users/login.html')

def register_view(request):
    return render(request,'users/register.html')