from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .forms import RegisterForm, ProductForm, ProductFormReview, ProfileForm
from django.contrib.auth import authenticate, logout, login
from .models import Product, Review, Profile
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator

def admin_required(view_function):
    return user_passes_test(lambda u: u.is_superuser)(view_function)


def index(request):
    products = Product.objects.all()
    new_products = Product.objects.filter(new=True)    
    context = {
        'products': products,
        'new_products': new_products,
    }
    return render(request, 'Shop/index.html', context)

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
                response = redirect("index")
                response.set_cookie('username', username, max_age=999999)
                return response
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

@admin_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
            form = ProductForm()
    return render(request, 'Shop/admin.html', {'form': form})


def paginator(request):
    prod = Product.objects.all()
    paginator = Paginator(prod, 3)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(request, 'Shop/paginator.html', {'page':page})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request=request, user=user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'Shop/change_password.html', {'form': form})