from django.db import models

class Courses(models.Model):
	title = models.CharField(max_length=255)
	fees = models.IntegerField()
	duration = models.IntegerField()
	instructor = models.CharField(max_length=255)
	img_url = models.CharField(max_length=2083)

	def __str__(self):
		return self.title


class Contact(models.Model):
	f_name = models.CharField(max_length=255)
	l_name = models.CharField(max_length=255)
	ph_no = models.IntegerField()
	email = models.EmailField()
	address = models.TextField()

	def __str__(self):
		return self.f_name + self.l_name