from attr import field
from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']