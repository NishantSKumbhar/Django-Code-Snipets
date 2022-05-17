from django.db import models

class Movies(models.Model):
	name = models.CharField(max_length=255)
	producer = models.CharField(max_length=255)
	duration = models.FloatField()
	image_url = models.CharField(max_length=2083)
	rated = models.CharField(max_length=5)
	info = models.CharField(max_length=120)
