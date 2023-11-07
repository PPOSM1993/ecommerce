from django.urls import path
from . import views

urlpatterns = [
    path('menu_cart/<int:product_id>/', views.AddToCart, name='menu_cart')
]
