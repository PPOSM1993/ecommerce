from django.shortcuts import render

# Create your views here.
from .cart import Cart

def AddToCart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    return render(request, 'cart/menu_cart.html')