from django.shortcuts import render

# Create your views here.

def login(request):
	return render(request, 'WePongAuth/login.html')

def homepage(request):
	return render(request, 'WePongAuth/homepage.html')

def registration(request):
	return render(request, 'WePongAuth/registration.html')