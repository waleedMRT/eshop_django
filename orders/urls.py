from django.urls import path
from .views import checkout , my_orders

urlpatterns = [
    path('checkout/' , checkout , name='ckeckout' ),
    path('my_orders/' , my_orders , name='my_orders')
]