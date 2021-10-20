from django.db import models

# Create your models here.
class Post(models.Model):
	headline = models.SlugField(max_length=30)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.headline

class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name