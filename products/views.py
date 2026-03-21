from django.shortcuts import render , get_object_or_404
from django.core.paginator import Paginator
from .models import *


def all_products(request):
    products = Product.objects.all()

    paginator = Paginator(products , 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products' : page_obj
    }
    return render(request , 'products/all_products.html' , context)

def product_details(request , id):
    product = get_object_or_404(Product , id=id)
    context = {
        'product' : product
    }
    return render(request , 'products/product_details.html' , context)


def search(request):
    query = request.GET.get('search')
    results = Product.objects.filter(name__icontains=query)
    context={
        'query' : query,
        'results' : results
    }
    return render(request , 'products/search.html' , context)

def categories_view(request , id):
    category = get_object_or_404(Category , id=id)
    products = Product.objects.filter(category=category)
    context = {
        'products' : products
    }
    return render(request , 'products/category.html' , context )

# Create your views here.
