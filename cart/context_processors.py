from .models import Cart

def cart_count(request):
    if request.user.is_authenticated:
        cart , created = Cart.objects.get_or_create(user=request.user)
        total_items = cart.items.count()
        return{
            'total_items' : total_items
        }
    return {
        'total_items' : 0
    }