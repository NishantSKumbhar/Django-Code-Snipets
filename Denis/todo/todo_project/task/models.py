from django.db import models
from django.utils import timezone
class Task(models.Model):
	name = models.CharField(max_length=255)
	completed = models.BooleanField(default=False)
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name
