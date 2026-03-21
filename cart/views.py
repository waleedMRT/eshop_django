from django.shortcuts import render , redirect , get_object_or_404
from products.models import Product
from .models import CartItem , Cart
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request , id):
    product = get_object_or_404(Product , id=id)
    cart , created = Cart.objects.get_or_create(user=request.user)
    cart_item , created = CartItem.objects.get_or_create(product=product , cart=cart)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')
    


@login_required
def cart_view(request):
    cart , created = Cart.objects.get_or_create(user=request.user)

    items = cart.items.all()
    context={
        'items' : items,
        'cart' : cart,
    }
    return render(request , 'cart/cart.html' , context)

login_required
def delete_cart_item(request , id):
    cart_item = get_object_or_404(CartItem , id=id)
    cart_item.delete()
    return redirect('cart')

@login_required
def increase_quantity(request , id):
    cart_item = get_object_or_404(CartItem , id=id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

@login_required
def decrease_quantity(request , id):
    cart_item = get_object_or_404(CartItem , id=id)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')
# Create your views here.
