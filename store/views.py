from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms
#great Work ya BRo , kept it up
def category_summary(request):
    categories = Category.objects.all()
    return render(request, 'category_summary.html', {"categories":categories})




def category(request, foo):
    #replace hyphens with spaces
    foo = foo.replace('-', ' ')
    # grab the category for the url
    try:
        # lookup the category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products,'category':category})

    except:
        messages.success(request,("That category doesn't exist!"))
        return redirect('home')

def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})



def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})


def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,("You Have been Logged In"))
            return redirect('home')
        else:
            messages.success(request,("There was an error, please try again"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request,("You have been logged out, Thanks."))
    return redirect('home')


def all_products(request):
    # Fetch all products from the database
    products = Product.objects.all()
    # Pass the products to the template for rendering
    return render(request, 'all_products.html', {'products': products})



def popular_items(request):
    popular_products = Product.objects.filter(views_count__gt=0).order_by('-views_count')[:10]
    return render(request, 'popular_items.html', {'popular_products': popular_products})




def new_arrivals(request):
    # Query the database for new arrivals (assuming you have a 'created_at' field in your Product model)
    new_arrival_products = Product.objects.order_by('-created_at')[:10]
    # Pass the new arrival products to the template for rendering
    return render(request, 'new_arrivals.html', {'new_arrival_products': new_arrival_products})


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,("You have Registered successfully."))
            return redirect("home")
        else:
            messages.success(request,("Whoooops!, There was a problem, please try again"))
            return redirect('register')

    else:
        return render(request, 'register.html', {'form':form})

