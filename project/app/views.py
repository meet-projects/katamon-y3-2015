from django.shortcuts import render, HttpResponse, redirect
from django.utils.datastructures import MultiValueDictKeyError

from app.models import Account, User, Event

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import datetime
import pdb


# Create your views here.

def home(request):
    dictionary = {"active": "homeTab"}
    return render(request, 'app/home.html', dictionary)


def login_page(request):
    dictionary = {"active": "LoginTab",
                  "organization_login": False, "action": "/login2/"}
    return render(request, 'app/login.html', dictionary)


def organization_login_page(request):
    dictionary = {"active": "OrganizationLoginTab",
                  "organization_login": True, "action": "/organizationLoginRequest/"}
    return render(request, 'app/login.html', dictionary)


def logoutrequest(request):
    dictionary = {"active": "LogOutTab"}
    logout(request)
    return redirect("/")


def UserProfile(request):
    dictionary = {"active": "UserProfileTab", "user": request.user}
    return render(request, 'app/UserProfile.html', dictionary)


def signup(request):
    if request.user.is_authenticated():
        return redirect("/home/")
    dictionary = {"active": "registerTab"}
    return render(request, 'app/signup.html', dictionary)


def addEvent(request):
    dictionary = {"active": "registerTab"}
    if request.user.is_authenticated() and request.user.account.isOrganization == True:
        return render(request, 'app/addevent.html', dictionary)
    return redirect("/home/")


def aboutus(request):
    dictionary = {"active": "aboutUsTab"}
    return render(request, 'app/aboutus.html', dictionary)


def events(request):
    dictionary = {"active": "eventsTab"}
    dictionary["events"] = Event.objects.all()
    return render(request, 'app/Events.html', dictionary)


def manage_events(request):
    dictionary = {"active": "manageEventsTab"}
    dictionary["events"] = Event.objects.all()
    return render(request, 'app/manageEvents.html', dictionary)


def volunteam(request):
    dictionary = {"active": "VolunTeamTab"}
    return render(request, 'app/volunteam.html', dictionary)

def photos(request):
    dictionary = {"active": "PhotosTab"}
    return render(request, 'app/photos.html', dictionary)

def OrgSignUp(request):
    if request.user.is_authenticated():
        return redirect("/home/")
    dictionary = {"active": "OrgSignUp"}
    return render(request, 'app/OrgSignUp.html', dictionary)


def addEvent_request(request):
    dictionary = {"active": "manageEventsTab"}

    eventName = request.POST.get('eventName')
    description = request.POST.get('description')
    address = request.POST.get('location')
    duration = request.POST.get('duration')
    dateDay = request.POST.get('dateDay')
    dateMonth = request.POST.get('dateMonth')
    dateYear = request.POST.get('dateYear')
    dateHour = request.POST.get('dateHour')
    dateMinute = request.POST.get('dateMinute')
    group_size = request.POST.get('groupSize')

    if not request.user.account.isOrganization:
        return HttpResponse("This account doesn't have the permission to do that.")
    organization = request.user.account

    if eventName is None or description is None or address is None or duration is None or dateDay is None or dateMonth is None or dateYear is None:
        dictionary["errors"] = ["Some of the fields are empty."]
        return render(request, 'app/addevent.html', dictionary)

    date = datetime.datetime(
        int(dateYear), int(dateMonth), int(dateDay), int(dateHour), int(dateMinute))

    event = Event.addEvent(
        eventName, date, duration, address, description, None, group_size, organization)
    event.save()
    return redirect("/manageEvents/")


def managment(request):
    if request.user.is_authenticated():
        dictionary = {"active": "managementTab"}
        return render(request, 'app/managment.html', dictionary)
    else:
        return redirect("/login")




@login_required
def managment2(request):
    dictionary = {"active": "registerTab"}
    user = request.user
    newFN = request.POST.get('FN')
    newLN = request.POST.get('LN')
    # newEmail=request.POST.get('NewEmail')
    OldPassword = request.POST.get('OldPassword')
    NewPassword = request.POST.get('NewPassword')
    ConfirmPassword = request.POST.get('ConfirmPassword')
    c = ""
    if newFN is None:
        newFN = user.first_name
        c += "s"
    if newLN is None:
        newLN = user.last_name
        c += "e"
    if OldPassword is None:
        NewPassword = user.password
        c += "v"
    if len(c) is 3:
        dictionary["errors"] = []
        dictionary["errors"].append("You did not change anything.")
        return render(request, 'app/managment.html', dictionary)
    if not user.check_password(OldPassword):
        dictionary["errors"] = []
        dictionary["errors"].append("Old password is incorrect.")
        return render(request, 'app/managment.html', dictionary)
    if (NewPassword != ConfirmPassword):
        dictionary["errors"] = []
        dictionary["errors"].append("Passwords do not match.")
        return render(request, 'app/managment.html', dictionary)
    if (len(NewPassword) < 6):
        dictionary["errors"] = []
        dictionary["errors"].append("password min 6 charecters.")
        return render(request, 'app/managment.html', dictionary)

    # if newEmail is None:
        # newEmail=user.email
    # user_obj = User(first_name=newFN, last_name=newLN) #email=newEmail,
    # username=newEmail
    request.user.first_name = newFN
    request.user.last_name = newLN

    request.user.set_password(NewPassword)
    request.user.save()
    # authenticate(username=newEmail, password=NewPassword)
    dictionary["errors"] = []
    dictionary["errors"].append("Changed successfully.")
    return render(request, 'app/managment.html', dictionary)


def OrgSignUpRequest(request):
    dictionary = {"active": "registerTab"}
    name = request.POST.get('OrganizationName')
    email = request.POST.get('OrganizationEmail')
    password = request.POST.get('OrganizationPassword')
    address = request.POST.get('OrganizationAddress')
    phone_number = request.POST.get('OrganizationPhoneNumber')
    description = request.POST.get('OrganizationDescription')
    website = request.POST.get('OrganizationWebsite')
    if name is None or password is None or address is None or phone_number is None or description is None:
        dictionary["errors"] = ["Some of the fields are empty."]
        return render(request, 'app/OrgSignUp.html', dictionary)
    if website is None:
        website = ""
    if (User.objects.filter(email=email).count() != 0):
        dictionary["errors"] = [
            "This Organization already exists, redirected to login page"]
        return render(request, 'app/OrgSignUp.html', dictionary)
    organization_obj = Account(
        address=address, phone_number=phone_number, description=description, website=website, isOrganization=True)

    user_obj = User(username=email, email=email)
    user_obj.set_password(password)
    user_obj.save()

    organization_obj.user = user_obj

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

    if firstName is None or lastName is None or password is None or email is None or birthdayDay is None or birthdayMonth is None or birthdayYear is None or nationality is None:
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


def login2(request):
    dictionary = {"active": "LoginTab"}
    try:
        email = request.POST['emailAddress']
        password = request.POST['password']
    except MultiValueDictKeyError:
        return redirect("/login")
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


def organization_login_request(request):
    dictionary = {"active": "LoginTab"}
    try:
        email = request.POST['emailAddress']
        password = request.POST['password']
    except MultiValueDictKeyError:
        return redirect("/organizationLogin")
    organization = authenticate(
        username=email, password=password, isOrganization=False)
    if organization is not None:
        # user and password is correct
        login(request, organization)
        return redirect("/events")
    else:
        # the authentication system was unable to verify the username and
        # password
        return redirect("/organizationLogin")


def showUsers(request):
    return render(request, 'app/showUsers.html', {"Accounts": Account.objects.all()})
