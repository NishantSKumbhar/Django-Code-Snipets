from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='product-home'),
    path('new/', views.new),
]
