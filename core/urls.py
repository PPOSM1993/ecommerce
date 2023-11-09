from django.contrib.auth import views
from django.urls import path
from . import views




urlpatterns = [
    path('', views.FrontPage, name='frontpage'),
    path('signup/', views.SignUp, name='signup'),
    path('shop/', views.Shop, name='shop'),
    path('about/', views.AboutUs, name='about'),
]
