from django.db import models
import datetime

# Create your models here.
class Account(models.Model):
	name = models.CharField(max_length=30)
	emailAddress = models.EmailField(unique=True)
	password = models.CharField(max_length=30)
	# Palestinian = true, Israeli = false
	isPalestinian = models.BooleanField()
	birthday = models.DateTimeField()

	def __unicode__(self):
		return self.name + " " + self.emailAddress + " " + str(self.birthday)
