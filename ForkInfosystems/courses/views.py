from django.shortcuts import render, redirect
from .models import Courses, Contact
from .forms import CourseForm, ContactForm




def home(request):
	course = Courses.objects.all()
	
	context = {
		'title' : "Home Page",
		'courses' : course,
		
	}
	return render(request, 'courses/index.html', context)


def contact(request):
	contact = Contact.objects.all()
	form = ContactForm()
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()

		return redirect('/')
	context = {
		'title' : "Contact Page",
		'contact' : contact,
		'form' : form
	}
	return render(request, 'courses/contact.html', context)


def add_course(request):

	course = Courses.objects.all()
	form = CourseForm()

	if request.method == "POST":
		form = CourseForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {
		'title' : "Add Course Page",
		'form' : form ,
		'course' : course
	}
	return render(request, 'courses/add_course.html', context)


def update_course(request, pk):
	course = Courses.objects.get(id=pk)
	form = CourseForm(instance=course)
	if request.method == "POST":
		form = CourseForm(request.POST, instance=course)
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {
		'title' : "Update Courses",
		'form' : form
	}
	
	return render(request, 'courses/update_course.html', context)

def dashboard(request):
	context = {
		'title' : 'DashBoard'
	}
	return render(request, 'courses/dashboard.html', context)


def delete_course(request, pk):
	course = Courses.objects.get(id=pk)
	if request.method == 'POST':
		course.delete()

		return redirect('/')

	context = {
		'item' : course
	}
	return render(request, 'courses/delete.html', context)