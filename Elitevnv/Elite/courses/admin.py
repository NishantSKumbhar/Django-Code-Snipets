from django.contrib import admin

from .models import Courses

class CoursesAdmin(admin.ModelAdmin):
	list_display = ('name', 'instructor', 'fees', 'duration', 'mode')


admin.site.register(Courses, CoursesAdmin)
