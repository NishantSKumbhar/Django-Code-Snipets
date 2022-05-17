from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.home, name='product-home'),
    path('about/', views.about, name='about'),
]   
