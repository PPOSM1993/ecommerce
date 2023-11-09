from django.urls import path
from .views import AddToCart, Cart

urlpatterns = [
    path('add_to_cart/<int:product_id>/', AddToCart, name='add_to_cart'),
    path('cart/', Cart, name='cart'),
]
