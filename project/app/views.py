from django.shortcuts import render, HttpResponse, redirect
from django.utils.datastructures import MultiValueDictKeyError

from models import Account, User, Event
from django.contrib.auth import authenticate, login, logout

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
    #dictionary = {"active" : "OrgSignUp" }
    return render(request, 'app/OrgSignUp.html', {})


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
        return render(request, 'app/signup.html', dictionary)

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
        #user and password is correct
        login(request, user)
        return redirect("/events")
    else:
        # the authentication system was unable to verify the username and
        # password
        return redirect("/login")


def showUsers(request):
    return render(request, 'app/showUsers.html', {"Accounts": Account.objects.all()})
