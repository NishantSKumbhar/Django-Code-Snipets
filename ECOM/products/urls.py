from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="product-home"),
    path('register/', views.register_user, name="registration"),
    path('products/', views.product_list, name="product-list"),
    path('add-products/', views.product_add, name="product-add"),
    path('update-product/<str:pk>', views.update_product, name="product-update"),
    path('delete-product/<str:pk>', views.delete_product, name="product-delete")
]