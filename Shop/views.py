from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .forms import RegisterForm, ProductForm, ProductFormReview, ProfileForm
from django.contrib.auth import authenticate, logout, login
from .models import Product, Review, Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


def index(request):
    products = Product.objects.all()    
    return render(request, 'Shop/index.html', {'products': products})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'Shop/register.html', {'form': form})


def login_p(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="Shop/login.html", context={"login_form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("index")



def add_produckt(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
            form = ProductForm()
    return render(request, 'main/admin_page.html', {'form': form})