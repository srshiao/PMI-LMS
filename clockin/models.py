import datetime
from django.db import models

class Intern(models.Model):
	def __str__(self):
   		return self.FName + " " + self.LName

	FName = models.CharField(("First Name"), max_length = 50, default = None)
	LName = models.CharField(("Last Name"), max_length = 50, default = None)
	username = models.CharField(("Username"), max_length = 50, default = None)
	team = models.CharField(("Team"), max_length = 50, default = None)
	#TODO: scores/stats

class Resource(models.Model):
	def __str__(self):
		return self.title + " by " + self.author
	title = models.CharField(("title"), max_length = 100, default = None)
	author = models.CharField(("Author"), max_length = 50, default = None)
	uploadDate = models.DateField(("Date"), default=datetime.date.today)
	urls = models.URLField(("url"), max_length = 150, default = None)
	#TODO: maybe put some stuff in it

class Video(models.Model):
	def __str__(self):
		return self.title + " by " + self.author
	title = models.CharField(("Title"), max_length = 100, default = None)
	author = models.CharField(("Author"), max_length = 50, default = None)
	#TODO: optional team field
	category = models.CharField(("Category"), max_length = 100, default = None)
	length = models.DurationField(("Length"), max_length = 50, default = None)
	upload_date = models.DateField(("Upload Date"), max_length = 50, default = None)
	urls = models.URLField(("url"), max_length = 150, default = None)
	video = models.FileField(("Video"), max_length = 100, default = None)
	
class QuizTest(models.Model):
	def __str__(self):
		return self.title + " by " + self.author
	title = models.CharField(("Title"), max_length = 100, default = None)
	author = models.CharField(("Author"), max_length = 50, default = None)
	#TODO: optional team field
	category = models.CharField(("Category"), max_length = 100, default = None)
	#TODO: questions list field
	#TODO: answers list field
	description = models.CharField(("Description"), max_length = 500, default = None)
	
	length = models.DurationField(("Length"), max_length = 50, default = None)
	upload_date = models.DateField(("Upload Date"), max_length = 50, default = None)
	urls = models.URLField(("url"), max_length = 150, default = None)
	video = models.FileField(("Video"), max_length = 100, default = None)
	rating = models.DecimalField("Rating", max_digits = 3, decimal_places = 2, default = None)
	count = models.IntegerField(("Rating"), default = None)
	















