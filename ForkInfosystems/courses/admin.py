from django.contrib import admin
from .models import Courses, Contact

class CoursesAdmin(admin.ModelAdmin):
	list_display = ('title', 'fees', 'duration')

class ContactAdmin(admin.ModelAdmin):
	list_display = ('f_name', 'l_name', 'email', 'ph_no')

admin.site.register(Courses, CoursesAdmin)
admin.site.register(Contact, ContactAdmin)
