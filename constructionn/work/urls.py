from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='work-home'),
    path('about/', views.about, name='work-about'),
    path('company/', views.company, name='work-company'),
    path('our_businesses/', views.businesses, name='work-businesses'),
    path('product_&_services/', views.ps, name='work-ps'),
    path('careers/', views.careers, name='work-careers'),

]