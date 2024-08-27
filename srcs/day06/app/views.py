from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import time
import random
from django.conf import settings
# Create your views here.
def homepage(request):
	current_time = time.time()
	if 'username' not in request.session or current_time - request.session['creation_time'] > 5:
		request.session['username'] = random.choice(settings.USER_NAMES)
		request.session['creation_time'] = current_time
		request.session.modified = True
	user = request.session['username']
	return render(request, 'app/homepage.html',{'user': user, 'time': request.session['creation_time']})

# def get_name(request):
# 	username = request.session.get('username')
# 	# print(f"<<<<{username}>>>>")
# 	print(f"Session Data: {request.session.items()}")
# 	return JsonResponse({'name':username})