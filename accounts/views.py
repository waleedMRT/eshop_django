from django.shortcuts import render , redirect , get_object_or_404
from .forms import RegisterForm , LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from products.models import Product , Category


def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {
        'products' : products ,
        'categories' : categories
    }
    return render(request , 'accounts/home.html' , context)

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request , 'You have been created an account successfuly')
            redirect('home')

    else:
        form = RegisterForm()
    
    context = {
        'form' : form
    }
    return render(request , 'accounts/register.html' , context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(
                request,
                username=username,
                password=password
            )
            if user is not None:
                login(request , user)
                messages.success(request , 'You have logged in successfully')
                return redirect('home')
            else:
                messages.error(request , 'Invalid username or password')
    else:
        form = LoginForm()
    context = {
        'form' : form
    }
    return render(request , 'accounts/login.html' , context)

def logout_view(request):
    logout(request)
    return redirect('home')

# Create your views here.
