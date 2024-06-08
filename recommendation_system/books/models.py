from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Emenitites(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Books(models.Model):
	book_name =models.CharField(max_length=100)
	book_description = models.TextField()
	book_image = models.CharField(max_length=500)
	price = models.IntegerField()
	emenities = models.ManyToManyField(Emenitites)
	
	def __str__(self):
		return self.book_name

