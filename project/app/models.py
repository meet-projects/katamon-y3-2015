from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Account(models.Model):

    # REGULAR CUSTOMERS FIELDS
    isPalestinian = models.BooleanField(default="")
    # birthday = models.DateTimeField()

    # ORGANIZATIONS FIELDS
    name = models.CharField(max_length=30, default="")
    phone_number = models.CharField(max_length=15, default="")
    address = models.CharField(max_length=60, default="")
    description = models.CharField(max_length=300, default="")
    # logo = models.FileField(upload_to='app/static/app/img')
    website = models.CharField(max_length=100, default="")

    # BOTH FIELDS
    user = models.OneToOneField(User)
    isOrganization = models.BooleanField(default=False)

    # TODO - ensure uniqueness in user field.

    def __unicode__(self):
        return self.user.username + " " + self.user.email + " "
        # + str(self.birthday)
# Event model


class EventCategory(models.Model):
    name = models.CharField(max_length=30)

    def getCategoryClassName(self):
        return self.name.replace(" ", "_") + "-category"


class Event(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField()
    duration = models.IntegerField()
    address = models.CharField(max_length=60)
    description = models.CharField(max_length=300)
    accounts = models.ManyToManyField(Account, related_name='customer_events')
    category = models.ForeignKey(EventCategory, null=True)

    group_size = models.IntegerField()
    organization = models.ForeignKey(
        Account, default=None, related_name='org_events')

    @staticmethod
    def addEvent(name, date, duration, address, description, accounts, group_size, organization, category):
        event = Event()
        event.name = name
        event.date = date
        event.duration = duration
        event.address = address
        event.description = description
        if not accounts is None:
            event.accounts.add(accounts)
        event.group_size = group_size
        event.organization = organization
        event.category = EventCategory.objects.get(id=category)

        return event

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

        htmlClasses.append(self.category.getCategoryClassName())

        return htmlClasses

# Org model


class Chat(models.Model):
    event = models.OneToOneField(Event)
    title = models.CharField(max_length=30)


class Message(models.Model):
    chat = models.ForeignKey(Chat)
    account = models.ForeignKey(Account)
    message = models.TextField()


class Badge(models.Model):
    name = models.CharField(max_length=30)
    account = models.ManyToManyField(Account)

    class Meta:
        abstract = True


class VolunteerHoursBadge(Badge):
    hours_requirement = models.IntegerField()


class VolunteerTimesBadge(Badge):
    times_requirement = models.IntegerField()
