from django.urls import path
from .views import add_to_cart , cart_view , delete_cart_item , increase_quantity , decrease_quantity

urlpatterns = [
    path('add/<int:id>' , add_to_cart , name='add_to_cart'),
    path('' , cart_view , name='cart' ),
    path('delete/<int:id>' , delete_cart_item , name='delete_cart_item' ),
    path('increase/<int:id>' , increase_quantity , name='increase_quantity' ),
    path('decrease/<int:id>' , decrease_quantity , name='decrease_quantity' ),

]