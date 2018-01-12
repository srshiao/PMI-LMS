import datetime
from django.utils import timezone
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User
from .fields import OrderField


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

##############	Models below this line are as per blueprint	##############

class Category(models.Model):
	def __str__(self):
   		return self.title

	title = models.CharField(("Title"), max_length = 200, default = None, unique = true)
	slug = models.SlugField(("Slug"), max_length = 200, default = None)
	overview = models.TextField(("Overview"), blank = true)
	
class Course(models.Model):
	def __str__(self):
   		return self.title

	owner = models.ForeignKey("User", related_name='courses_created')	#UNSURE
 	category = models.ForeignKey("Category", related_name='courses')	#UNSURE
   	title = models.CharField(("Title"), max_length = 200, default = None, unique = true)
	slug = models.SlugField(("Slug"), max_length = 200, default = None)
	overview = models.TextField(("Overview"), blank = true)
	created = models.DateField(_("Created"), default= datetime.date.today)	

class Module(models.Model):
	def __str__(self):
   		return '{ }.{ }'.format(self.order,self.title)

	course = models.ForeignKey("Course", related_name='modules')	#UNSURE
   	title = models.CharField(("Title"), max_length = 200, default = None)
	description = models.TextField(("Description"), blank = true)
	order = models.OrderField(("Order"), blank = true, for_fields = ['course'])

class Content(models.Model):
	def __str__(self):
   		return '{ }.{ }'.format(self.order,self.title)

	module = models.ForeignKey("Module", related_name='contents')	#UNSURE
   	content_type = models.ForeignKey("ContentType", limit_choices_to={'model__in':('text','video','image','file')})
   	object_id = models.PositiveIntegerField("ObjectType", default = None)
 	item = GenericForeignKey("content_type", "object_id")
	order = models.OrderField(("Order"), blank = true, for_fields = ['module'])
	
class Quiz(models.Model):
	def __str__(self):
   		return self.title

	title = models.CharField(("Title"), max_length = 200, default = None)
	total_score = models.IntegerField("TotalScore", default = None)
	result = models.CharField(("Result"), max_length = 200, default = None)

class Certificate(models.Model):
	def __str__(self):
   		return self.title

	title = models.CharField(("Title"), max_length = 200, default = None, unique = true)
	course = models.ForeignKey("Course", related_name='certificates')	#UNSURE
	issued_on = models.DateField(_("IssuedOn"), default= datetime.date.today)
	
class Text(models.Model):
	content = models.TextField(("Content"), max_length = 200, default = None)

class File(models.Model):
	file = models.FileField(("File"), upload_to='files', default = None)

class Video(models.Model):
	url = models.URLField(("URL"), default = None)

class Image(models.Model):
	image = models.ImageField(("Image"), upload_to='images', default = None)
 	
class ItemBase(models.Model):
	def __str__(self):
   		return self.title

	title = models.CharField(("Title"), max_length = 200, default = None)
	owner = models.ForeignKey("User", related_name='itembases')	#UNSURE
	created = models.DateField(_("Created"), default= datetime.date.today)
	updated = models.DateField(_("Updated"), default= datetime.date.today)

class Question_Answer(models.Model):
	def __str__(self):
   		return self.question

	question = models.TextField(("Question"), max_length = 200, default = None)
	option1 = models.TextField(("Option1"), max_length = 200, default = None)
	option2 = models.TextField(("Option2"), max_length = 200, default = None)
	option3 = models.TextField(("Option3"), max_length = 200, default = None)
	option4 = models.TextField(("Option4"), max_length = 200, default = None)
	answer = models.TextField(("Answer"), max_length = 200, default = None)
	answer_desc = models.TextField(("AnswerDesc"), max_length = 200, default = None)
	score = models.IntegerField("Score", default = None)
	quiz = models.ForeignKey("Quiz", related_name='question_answers')	#UNSURE
