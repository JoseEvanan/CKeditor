from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TextEquation(models.Model):
	head = models.CharField(max_length=250)
	equation = models.CharField(max_length=250)

	def __str__(self):
		return str(self.equation)