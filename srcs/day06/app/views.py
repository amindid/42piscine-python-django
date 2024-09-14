from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate,logout, login as auth_login 
import time
import random
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages

def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		try :
			user = User.objects.get(username=username)
			password = request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				auth_login(request,user)
				request.session['username'] = username
				request.session['creation_time'] = time.time()
				return redirect('homepage')
			else:
				messages.error(request, 'incorrect password !!')
				return render(request, 'app/login.html')
		except Exception as e:
			messages.error(request, 'user dose not exist')
			redirect('login')

	return render(request, 'app/login.html')
def registration(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		if User.objects.filter(username=username).exists():
			messages.error(request, 'Username is already in use')
			return render(request, 'app/registration.html')
		password = request.POST.get('password')
		confirm_password = request.POST.get('confirm_password')
		if password != confirm_password:
			messages.error(request, 'password confirmation dose not match the password !!')
			return render(request, 'app/registration.html')
		user = User.objects.create_user(username=username, password=password)
		user.save()
		auth_login(request, user)
		request.session['username'] = username
		request.session['creation_time'] = time.time()
		return redirect('homepage')

	return render(request, 'app/registration.html')

def homepage(request):
	if request.user.is_authenticated:
		return render(request, 'app/homepage.html',{'user': request.user.username, 'bool' : True})
	current_time = time.time()
	if 'username' not in request.session or current_time - request.session['creation_time'] > 5:
		request.session['username'] = random.choice(settings.USER_NAMES)
		request.session['creation_time'] = current_time
		request.session.modified = True
	user = request.session['username']
	return render(request, 'app/homepage.html',{'user': user, 'bool': False})

def logout_view(request):
	logout(request)
	return redirect('homepage')