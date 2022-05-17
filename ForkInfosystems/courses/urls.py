from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="courses-home"),
    path('contact/', views.contact, name="courses-contact"),
    path('addCourse/', views.add_course, name="courses-add"),
    path('dashboard/', views.dashboard, name="courses-dashboard"),
    path('updateCourse/<str:pk>/', views.update_course, name="courses-update"),
    path('deleteCourse/<str:pk>/', views.delete_course, name="courses-delete"),
]