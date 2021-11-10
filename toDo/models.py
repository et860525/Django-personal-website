from django.db import models

# Create your models here.
class Task(models.Model):
	name = models.CharField(max_length=100)
	detail = models.CharField(max_length=150, null=True, blank=True)
	create_date = models.DateTimeField(auto_now_add=True)
	due_date = models.DateTimeField()

	def __repr__(self):
		return self.name