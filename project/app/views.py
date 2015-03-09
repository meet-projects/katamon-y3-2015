from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'app/home.html', {})

def login(request):
	return render(request, 'app/login.html', {})

def signup(request):
	return render(request, 'app/signup.html', {})

def aboutus(request):
	return render(request, 'app/aboutus.html', {})