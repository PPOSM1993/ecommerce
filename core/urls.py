from django.urls import path
from . import views


urlpatterns = [
    path('', views.FrontPage, name='frontpage'),
    path('shop/', views.Shop, name='shop'),
    #path('shop/<slug:slug>/', views.Product, name='product'),

    path('about/', views.AboutUs, name='about'),
]
