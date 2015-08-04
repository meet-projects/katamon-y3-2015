from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Account(models.Model):
    isPalestinian = models.BooleanField()
    # birthday = models.DateTimeField()
    user = models.OneToOneField(User)

    def __unicode__(self):

        return self.user.username + " " + self.user.email + " "
        # + str(self.birthday)
# Event model


class Organization(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=60)
    description = models.CharField(max_length=300)
    #logo = models.FileField(upload_to='app/static/app/img')
    website = models.CharField(max_length=100)


class Event(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField()
    duration = models.IntegerField()
    address = models.CharField(max_length=60)
    description = models.CharField(max_length=300)
    accounts = models.ManyToManyField(Account)
    group_size = models.IntegerField()
    organization = models.ForeignKey(Organization, default=None)

    def addEvent(self, name, date, duration, address, description, accounts, group_size, organization):
        self.name = name
        self.date = date
        self.duration = duration
        self.address = address
        self.description = description
        self.accounts.add(accounts)
        self.group_size = group_size
        self.organization = organization

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

# Org model


class Chat(models.Model):
    event = models.OneToOneField(Event)
    title = models.CharField(max_length=30)


class Message(models.Model):
    chat = models.ForeignKey(Chat)
    account = models.ForeignKey(Account)
    message = models.CharField(max_length=1000)


class Badge(models.Model):
    name = models.CharField(max_length=30)
    account = models.ManyToManyField(Account)

    class Meta:
        abstract = True


class VolunteerHoursBadge(Badge):
    hours_requirement = models.IntegerField()


class VolunteerTimesBadge(Badge):
    times_requirement = models.IntegerField()
