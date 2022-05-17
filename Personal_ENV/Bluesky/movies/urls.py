from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='movies-home'),
    path('about/', views.about, name='movies-about'),
    path('contact/', views.contact, name='movies-contact'),
    path('watchmovie/', views.watchmovie, name='movies-watchmovie'),
]