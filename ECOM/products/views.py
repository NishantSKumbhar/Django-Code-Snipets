from django.shortcuts import render, redirect
from requests import request
from .models import *
from .forms import CreateUserForm, ProductForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home(request):
    context = {
        'title' : 'Home | Products'
    }
    return render(request, 'products/index.html', context)


def product_list(request):
    
    product = Product.objects.all()

    context = {
        'title' : 'List | Products',
        'product' : product
    }

    return render(request, 'products/products.html', context)

def product_add(request):
    product = Product.objects.all()
    

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductForm()

    context = {
        'title' : 'Add | Products',
        'product' : product,
        'form' : form
    }

    return render(request, 'products/add_products.html', context)


def update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
        return redirect('/products')
    context = {
        'title' : 'Update | Products',
        'product' : product,
        'form' : form
    }

    return render(request, 'products/add_products.html', context)


def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()

        return redirect('/products')
    context = {
        'title' : 'Delete | Products',
        'product' : product,
        
    }

    return render(request, 'products/delete_product.html', context)

def register_user(request):
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Successfully Created {username}')
            return redirect('/')
    else:
        form = CreateUserForm()
    context = {
        'title' : 'Register | User',
        'form' : form
    }

    return render(request, 'products/register.html', context)