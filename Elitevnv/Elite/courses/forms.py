from django import forms 
from django.forms import ModelForm
from .models import *

class CoursesForm(forms.ModelForm):

	class Meta:
		model = Courses
		fields = '__all__'