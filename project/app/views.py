from django.shortcuts import render, HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from models import Account
import datetime



# Create your views here.
def home(request):
	return render(request, 'app/home.html', {})

def login(request):
	return render(request, 'app/login.html', {})

def signup(request):
	return render(request, 'app/signup.html', {})

def aboutus(request):
	return render(request, 'app/aboutus.html', {})

def volunteam(request):
	return render(request, 'app/volunteam.html', {})
def signupRequest(request):
	
	try:
		name = request.POST['name']
		password = request.POST['password']
		email = request.POST['emailAddress']
		birthdayDay = request.POST['birthdayDay']
		birthdayMonth = request.POST['birthdayMonth']
		birthdayYear = request.POST['birthdayYear']
		nationality = request.POST['nationality']
	except MultiValueDictKeyError:
		return HttpResponse("Not all of the fields were filled")
	

	if (name == "" or password == "" or email == "" or birthdayDay == "" or birthdayMonth == "" or birthdayYear == "" or nationality == ""):
		return HttpResponse("Some of the fields are empty.")

	if (nationality == "isra"):
		nationality = False
	else:
		nationality = True

	birthday = datetime.time(int(birthdayDay), int(birthdayMonth), int(birthdayYear))

	account_obj = Account(name = name, emailAdress = email, password = password, isPalestinian = nationality, birthday = birthday)
	account_obj.save()

	return HttpResponse("Banana")

