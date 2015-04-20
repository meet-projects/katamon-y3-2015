from django.db import models

# Create your models here.
class Account(models.Model):
	name = models.CharField(max_length=30)
	emailAdress = models.EmailField()
	password = models.CharField(max_length=30)
	# Palestinian = true, Israeli = false
	isPalestinian = models.BooleanField()
	birthday = models.DateTimeField()

