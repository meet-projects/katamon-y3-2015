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

# Event model
class Event(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField()
    duration = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    description = models.CharField(max_length=300)
    accounts = models.ManyToManyField(Account)

    def getHtmlClasses(self):
        dayClasses = ["monday-day", "tuesday-day", "wednesday-day",
                      "thursday-day", "friday-day", "saturday-day"]
        htmlClasses = []
        htmlClasses.append(dayClasses[self.date.weekday()])
        if self.date.hour < 12:
            htmlClasses.append("morning-time")
        elif self.date.hour < 14:
            htmlClasses.append("noon-time")
        elif self.date.hour < 16:
            htmlClasses.append("afternoon-time")
        elif self.date.hour < 18:
            htmlClasses.append("evening-time")
    # attendees

        htmlClasses.append("handicapped-field")

        return htmlClasses
# AddEvent model


class AddEvent(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=60)
    time = models.CharField(max_length=30)
    date = models.DateTimeField()

# Org model
class Organization(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=10)
    number = models.CharField(max_length=15)
    address = models.CharField(max_length=60)
    description = models.CharField(max_length=300)
    event = models.ManyToManyField(Event)
    #logo = models.FileField(upload_to='app/static/app/img')
    website = models.CharField(max_length=100)
