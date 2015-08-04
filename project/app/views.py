from django.shortcuts import render, HttpResponse, redirect
from django.utils.datastructures import MultiValueDictKeyError
from app.models import User
from models import Account, User, Event, Organization
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import datetime


# Create your views here.

def home(request):
    dictionary = {"active": "homeTab"}
    return render(request, 'app/home.html', dictionary)


def login_page(request):
    dictionary = {"active": "LoginTab"}
    return render(request, 'app/login.html', dictionary)


def login2(request):
    dictionary = {"active": "LoginTab"}
    try:
        email = request.POST['emailAddress']
        password = request.POST['password']
    except MultiValueDictKeyError:
        return redirect("/login")
    return login_request(request, email, password)


def logoutrequest(request):
    dictionary = {"active": "LogOutTab"}
    logout(request)
    return redirect("/")


def signup(request):
    dictionary = {"active": "registerTab"}
    return render(request, 'app/signup.html', dictionary)


def addevent(request):
    dictionary = {"active": "registerTab"}
    return render(request, 'app/addevent.html', dictionary)


def aboutus(request):
    dictionary = {"active": "aboutUsTab"}
    return render(request, 'app/aboutus.html', dictionary)


def events(request):
    dictionary = {"active": "eventsTab"}
    dictionary["events"] = Event.objects.all()
    return render(request, 'app/Events.html', dictionary)


def volunteam(request):
    dictionary = {"active": "VolunTeamTab"}
    return render(request, 'app/volunteam.html', dictionary)


def OrgSignUp(request):
    dictionary = {"active" : "OrgSignUp" }
    return render(request, 'app/OrgSignUp.html', dictionary)


def managment(request):
 if request.user.is_authenticated():
    dictionary = {"active": "managementTab"}
    return render(request, 'app/managment.html', dictionary)
 else :
	return redirect("/login")
@login_required
def managment2(request):
	dictionary = {"active": "registerTab"}
	user = request.user
	newFN=request.POST.get('FN')
	newLN=request.POST.get('LN')
	#newEmail=request.POST.get('NewEmail')
	OldPassword=request.POST.get('OldPassword')
	NewPassword=request.POST.get('NewPassword')
	ConfirmPassword=request.POST.get('ConfirmPassword')
	if not user.check_password(OldPassword):
		dictionary["errors"] = []
		dictionary["errors"].append("Old password is incorrect.")
		return render(request, 'app/managment.html', dictionary)
	if (NewPassword!=ConfirmPassword):
		dictionary["errors"] = []
		dictionary["errors"].append("Passwords do not match.")
		return render(request, 'app/managment.html', dictionary)
	if (len(NewPassword)<6):
		dictionary["errors"] = []
		dictionary["errors"].append("password min 6 charecters.")
		return render(request, 'app/managment.html', dictionary)
			
	if newFN is None:
		newFN=user.first_name
	if newLN is None:
		newLN=user.last_name
	if OldPassword is None:
		NewPassword=user.password
	#if newEmail is None:
		#newEmail=user.email
	#user_obj = User(first_name=newFN, last_name=newLN) #email=newEmail, username=newEmail
	request.user.first_name = newFN
	request.user.last_name = newLN
	
    	request.user.set_password(NewPassword)
    	request.user.save()
	#authenticate(username=newEmail, password=NewPassword)
	dictionary["errors"] = []
	dictionary["errors"].append("Changed successfully.")
	return render(request, 'app/managment.html', dictionary)
	


def OrgSignUpRequest(request):
    dictionary = {"active": "registerTab"}
    name = request.POST.get('OrganizationName')
    password = request.POST.get('OrganizationPassword')
    address = request.POST.get('OrganizationAddress')
    number = request.POST.get('OrganizationPhoneNumber')
    description = request.POST.get('OrganizationDescription')
    website = request.POST.get('website')
    if name is None \
           or \
           password is None or \
           address is None or \
           number is None or description is None:
        dictionary["errors"] = ["Some of the fields are empty."]
        return render(request, 'app/OrgSignUp.html', dictionary)
    if website is None :
	website=""
    if (Organization.objects.filter(name=name).count() != 0):
        dictionary["errors"] = [
            "This Organization already exists, redirected to login page"]
        return render(request, 'app/OrgSignUp.html', dictionary)
    organization_obj = Organization(name=name, password=password, address=address, number=number, description=description,website=website)
    organization_obj.save()
    return redirect("/events")



def signupRequest(request):
    dictionary = {"active": "registerTab"}

    firstName = request.POST.get('firstName')
    lastName = request.POST.get('lastName')
    password = request.POST.get('password')
    email = request.POST.get('emailAddress')
    birthdayDay = request.POST.get('birthdayDay')
    birthdayMonth = request.POST.get('birthdayMonth')
    birthdayYear = request.POST.get('birthdayYear')
    nationality = request.POST.get('nationality')

    if firstName is None \
            or \
            lastName is None or \
            password is None or \
            email is None or \
            birthdayDay is None or \
            birthdayMonth is None or \
            birthdayYear is None or nationality is None:
        dictionary["errors"] = ["Some of the fields are empty."]
        return render(request, 'app/signup.html', dictionary)

    if (User.objects.filter(email=email).count() != 0):
        dictionary["errors"] = [
            "Email Address already exists, redirected to login page"]
        return render(request, 'app/login.html', dictionary)

    if (nationality == "isra"):
        nationality = False
    else:
        nationality = True

    birthday = datetime.datetime(
        int(birthdayYear), int(birthdayMonth), int(birthdayDay))
    # birthday = datetime.datetime.now()
    user_obj = User(
        first_name=firstName, last_name=lastName, email=email, username=email)
    user_obj.set_password(password)
    user_obj.save()

    account_obj = Account(user=user_obj, isPalestinian=nationality)
    account_obj.save()
    return login_request(request, email, password)


def login_request(request, email, password):
    user = authenticate(username=email, password=password)
    if user is not None:
        # user and password is correct
        login(request, user)
        return redirect("/events")
    else:
        # the authentication system was unable to verify the username and
        # password
        return redirect("/login")

def Orglogin_request(request, name, password):
    Org = authenticate(username=name, password=password)
    if user is not None:
        # user and password is correct
        login(request, user)
        return redirect("/events")
    else:
        # the authentication system was unable to verify the username and
        # password
        return redirect("/login")


def showUsers(request):
    return render(request, 'app/showUsers.html', {"Accounts": Account.objects.all()})
