from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from .models import Order , OrderItem
from django.contrib import messages

@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    order = Order.objects.create(user=request.user , total_price = cart.total_cart_price())

    for item in cart.items.all():
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price,
        )
    
    cart.items.all().delete()
    messages.success(request , 'Your order have been placed successfuly')

    return redirect('all_products')

@login_required
def my_orders(request):
    orders = Order.objects.filter(user = request.user).order_by('-created_at')
    context = {
        'orders': orders
    }
    return render(request , 'orders/my_orders.html' , context)

# Create your views here.
