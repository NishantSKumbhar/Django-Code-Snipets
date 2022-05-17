from django import forms
from django.forms import ModelForm
from .models import Courses, Contact


class CourseForm(forms.ModelForm):
	class Meta:
		model = Courses
		fields = '__all__'

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'