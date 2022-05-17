from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def index(request):
	task = Task.objects.all()
	form = TaskForm()

	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {
		'tasks' : task,
		'form' : form,
		'title' : 'Home'
	}
	return render(request, 'task/home.html', context)

def updateTask(request, pk):
	task = Task.objects.get(id=pk)

	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST , instance=task)
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {
		'form' : form
	}

	return render(request, 'task/update.html', context)