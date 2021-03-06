from django.db import models

class Project(models.Model):
	"A project from our repository on Github"
	title = models.CharField(max_length=200)
	description = models.TextField()
	language = models.CharField(max_length=50)
	date_created = models.DateField(auto_now_add=False)
	size = models.IntegerField() 
	stars = models.IntegerField()

	def __str__(self):
		"Return a string representation of the model"
		return self.text