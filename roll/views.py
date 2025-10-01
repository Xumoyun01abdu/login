from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Products



def index(request):
    products = Products.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'index.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('index')

