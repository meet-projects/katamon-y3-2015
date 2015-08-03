from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Account(models.Model):
	isPalestinian = models.BooleanField()
	#birthday = models.DateTimeField()
	user = models.OneToOneField(User)
	def __unicode__(self):
		return self.user.username + " " + self.user.email + " " + str(self.birthday)

#Event model
class Event(models.Model):
	name = models.CharField(max_length=30)
	date = models.DateTimeField()
	time = models.CharField(max_length=30)
	address = models.CharField(max_length=60)
	description = models.CharField(max_length=300)
	accounts = models.ManyToManyField(Account)
	#attendees

#AddEvent model
class AddEvent(models.Model):
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=300)
	location = models.CharField(max_length=60)
	time = models.CharField(max_length=30)
	date = models.DateTimeField()

#Org model
class Organization(models.Model):
	name = models.CharField(max_length=30)
	number = models.CharField(max_length=15)
	address = models.CharField(max_length=60)
	description = models.CharField(max_length=300)
	event = models.ManyToManyField(Event)
	#logo = models.FileField(upload_to='app/static/app/img')
	website = models.CharField(max_length=100)

