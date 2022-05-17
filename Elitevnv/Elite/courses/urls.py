from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='courses-home'),
    path('about/', views.about, name='courses-about'),
    path('add_course/', views.add_course, name='courses-add'),
    path('update_course/<str:pk>', views.update_course, name='courses-update'),
]