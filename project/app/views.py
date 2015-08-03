from django.shortcuts import render, HttpResponse, redirect
from django.utils.datastructures import MultiValueDictKeyError
from models import Account, User
import datetime



# Create your views here.

def home(request):
	dictionary = {"active" : "homeTab" }
	return render(request, 'app/home.html', dictionary)

def login_page(request):
	dictionary = {"active" : "LoginTab" }
	return render(request, 'app/login.html', dictionary)

def login2(request):
	dictionary = {"active" : "LoginTab" }
	return render(request, 'app/Events.html', dictionary)

def signup(request):
	dictionary = {"active" : "registerTab" }
	return render(request, 'app/signup.html', dictionary)

def aboutus(request):
	dictionary = {"active" : "aboutUsTab" }
	return render(request, 'app/aboutus.html', dictionary)


def events(request):
	dictionary = {"active" : "eventsTab" }
	return render(request, 'app/Events.html', dictionary)


def volunteam(request):
	dictionary = {"active" : "VolunTeamTab" }
	return render(request, 'app/volunteam.html', dictionary)

def OrgSignUp(request):
	#dictionary = {"active" : "OrgSignUp" }
	return render(request, 'app/OrgSignUp.html', {} )


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

	if (nationality == "isra"):
		nationality = False
	else:
		nationality = True

	birthday = datetime.datetime(int(birthdayYear), int(birthdayMonth), int(birthdayDay))
	# birthday = datetime.datetime.now()
	user_obj = User(first_name = firstName, last_name = lastName, email = email, password = password, username = email)
	user_obj.save()

	account_obj = Account(user = user_obj, isPalestinian = nationality)
	account_obj.save()

	return HttpResponse("Banana")
def loginRequest(request):
	try:
		emailAddress = request.POST['emailAddress']
		password = request.POST['password']
	except MultiValueDictKeyError:
		return HttpResponse("Not all of the fields were filled")
	user = authenticate(username=emailAddress, password=password)
	if user is not None:
	    # the password verified for the user
	    if user.is_active:
		login(request, user)
		return redirect("/events")


	    else:
		return HttpResponse("The password is valid, but the account has been disabled!")
	else:
		
		return redirect("/volunteam/")
	


def showUsers(request):
	return render(request, 'app/showUsers.html', {"Accounts": Account.objects.all()})

