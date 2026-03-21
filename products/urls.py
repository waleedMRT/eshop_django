from django.urls import path
from .views import all_products , product_details , search , categories_view

urlpatterns = [
    path('' , all_products , name='all_products'),
    path('detail/<int:id>' , product_details , name='product_details'),
    path('search/' , search , name='search'),
    path('category/<int:id>' , categories_view , name='category' )
]