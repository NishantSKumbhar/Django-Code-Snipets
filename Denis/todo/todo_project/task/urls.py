from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='task-home'),
    path('update/<str:pk>/', views.updateTask, name='task-update'),
] 