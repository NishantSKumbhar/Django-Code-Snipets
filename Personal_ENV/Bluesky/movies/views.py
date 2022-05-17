from django.shortcuts import render
from .models import Movies

def home(request):
	context = {
		'title' : 'Home-page'
	}
	return render(request, 'movies/home.html', context)

def about(request):
	context = {
		'title' : 'About-page'
	}	
	return render(request, 'movies/about.html', context)


def contact(request):
	context = {
		'title' : 'Contact-page'
	}
	return render(request, 'movies/contact.html', context)


def watchmovie(request):
	movies = Movies.objects.all()
	context = {
		'movies' : movies
	}
	return render(request, 'movies/watchmovie.html', context)
