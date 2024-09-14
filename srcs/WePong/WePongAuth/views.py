from django.shortcuts import render, redirect
from .models import User, Stats
from django.contrib import messages
import hashlib
from django.contrib.sites.shortcuts import get_current_site
from .tokens import email_confirmation_token
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.core.mail import send_mail

# Create your views here.

def emailConfirmation(request):
	return render(request, 'WePongAuth/EmailConfirmation.html')

def hash_password(password):
	password_bytes = password.encode('utf-8')
	sha256 = hashlib.sha256()
	sha256.update(password_bytes)
	hashed_password = sha256.hexdigest()
	return hashed_password


def activate(request, uidb64,token):
	try:
		uid = force_str(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None

	if user is not None and email_confirmation_token.check_token(user, token):
		user.is_email_confirmed = True
		user.save()
		messages.success(request, 'email confirmed successfuly')
		return redirect('registration')
	else:
		messages.error(request, 'email activation is invalid')
		return redirect('registration')
	
def login(request):
	return render(request, 'WePongAuth/login.html')

def homepage(request):
	return render(request, 'WePongAuth/homepage.html')

def registration(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		if User.objects.filter(username=username).exists():
			messages.error(request, "Username already in use")
			return render(request, 'WePongAuth/registration.html')
		
		email = request.POST.get('email')
		if User.objects.filter(email=email).exists():
			messages.error(request, "email already in use")
			return render(request, 'WePongAuth/registration.html')
		
		password =  hash_password(request.POST.get('password'))
		confirm_password = hash_password(request.POST.get('passwordConfirmation'))
		if password != confirm_password:
			messages.error(request, "password confirmation dose not match the password")
			return render(request, 'WePongAuth/registration.html')
		
		user = User.objects.create(username=username,password=password,email=email)
		user.save()
		current_site = get_current_site(request)
		mail_subject = 'Activate your account.'
		token = email_confirmation_token.make_token(user)
		uid = urlsafe_base64_encode(force_bytes(user.pk))
		message = render_to_string('WePongAuth/email_confirmation.html', {
			'user' : user,
			'domain' : current_site,
			'uid' : uid,
			'token' : token,
		})
		try:
			send_mail(mail_subject, message, 'wepong10auth@gmail.com', [user.email])
			return render(request, 'WePongAuth/EmailConfirmation.html')
		except Exception as e:
			user.delete()
			print(f"<<<<{e}>>>>")
			messages.error(request, 'invalid credentials')
			return render(request, 'WePongAuth/registration.html')
		return redirect('homepage')
	return render(request, 'WePongAuth/registration.html')