from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def home(request):
	products = Product.objects.all()
	return render(request, 'index.html', {'products' : products})

def about(request):
	return HttpResponse('This is About Page')
