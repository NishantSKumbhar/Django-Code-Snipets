from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Courses
from .forms import CoursesForm


def home(request):
	course = Courses.objects.all()
	context = {
		'course' : course
	}
	return render(request, 'courses/home.html', context)

def about(request):
	context = {
		'title' : 'Lexcrop'
	}
	return render(request, 'courses/about.html', context)

def add_course(request):
	course = Courses.objects.all()
	form = CoursesForm()
	if request.method == 'POST':
		form = CoursesForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {
		'form' : form
	}

	return render(request, 'courses/add_courses.html', context)

def update_course(request, pk):
	course = Courses.objects.get(id=pk)
	form = CoursesForm(instance=course)

	if request.method == 'POST':
		form = CoursesForm(request.POST, instance=course)
		if form.is_valid():
			form.save()
		return redirect('/')
	context = {
		'form' : form
	}

	return render(request, 'courses/update.html', context)