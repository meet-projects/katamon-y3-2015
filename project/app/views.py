from django.shortcuts import render, HttpResponse, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from models import Account, User
import datetime



# Create your views here.

def home(request):
	dictionary = {"active" : "homeTab" }
	return render(request, 'app/home.html', dictionary)

def login(request):
	dictionary = {"active" : "LoginTab" }
	return render(request, 'app/login.html', dictionary)

def signup(request):
	dictionary = {"active" : "registerTab" }
	return render(request, 'app/signup.html', dictionary)

def aboutus(request):
<<<<<<< HEAD
		dictionary = {"active" : "aboutUsTab" }
		return render(request, 'app/aboutus.html', dictionary)

=======
	dictionary = {"active" : "aboutUsTab" }
	return render(request, 'app/aboutus.html', dictionary)
>>>>>>> e07ba074e523bef96c0cb1565dca722efd1510b5

@login_required
def events(request):
<<<<<<< HEAD
		dictionary = {"active" : "eventsTab" }
		return render(request, 'app/Events.html', dictionary)
	
=======
	dictionary = {"active" : "eventsTab" }
	return render(request, 'app/Events.html', dictionary)

>>>>>>> e07ba074e523bef96c0cb1565dca722efd1510b5
def volunteam(request):
		dictionary = {"active" : "VolunTeamTab" }
		return render(request, 'app/volunteam.html', dictionary)

def signupRequest(request):
	
	try:
		firstName = request.POST['firstName']
		lastName = request.POST['lastName']
		password = request.POST['password']
		email = request.POST['emailAddress']
		birthdayDay = request.POST['birthdayDay']
		birthdayMonth = request.POST['birthdayMonth']
		birthdayYear = request.POST['birthdayYear']
		nationality = request.POST['nationality']
	except MultiValueDictKeyError:
		return HttpResponse("Not all of the fields were filled")
	

	if (firstName == "" or lastName == "" or password == "" or email == "" or birthdayDay == "" or birthdayMonth == "" or birthdayYear == "" or nationality == ""):
		return HttpResponse("Some of the fields are empty.")

	isPalestinian = nationality != "isra"


	birthday = datetime.datetime(int(birthdayYear), int(birthdayMonth), int(birthdayDay))
	# birthday = datetime.datetime.now()
	user_obj = User.objects.create_user(email, email, password)
	user_obj.first_name = firstName
	user_obj.last_name = lastName
	user_obj.save()

	account_obj = Account(user = user_obj, isPalestinian = isPalestinian)
	account_obj.save()

	return HttpResponse("Banana")
def login2(request):
	try:
		emailAddress = request.POST['emailAddress']
		password = request.POST['password']
	except MultiValueDictKeyError:
		return HttpResponse("Not all of the fields were filled")


	user = authenticate(username=emailAddress, password=password)
	if user is not None:
	    # the password verified for the user
	    if user.is_active:
		return redirect("/events")
	    else:
		return HttpResponse("The password is valid, but the account has been disabled!")
	else:
	    # the authentication system was unable to verify the username and password
	    return HttpResponse("The username and password were incorrect.")


def showUsers(request):
	return render(request, 'app/showUsers.html', {"Accounts": Account.objects.all()})

