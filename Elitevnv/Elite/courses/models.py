from django.db import models

class Courses(models.Model):
	name = models.CharField(max_length=255)
	instructor = models.CharField(max_length=255)
	fees = models.FloatField(max_length=10)
	mode = models.CharField(max_length=10)
	duration = models.IntegerField()
	image_url = models.CharField(max_length=2083, default="")

	def __str__(self):
		return self.name
		