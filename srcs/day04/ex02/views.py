from django.shortcuts import render, redirect
from django.conf import settings
from datetime import datetime

# Create your views here.
from django import forms
import os

class theForm(forms.Form):
	text = forms.CharField(label='')

def form(request):
	if request.method == "POST":
		form = theForm(request.POST)
		if form.is_valid():
			with open(settings.HISTORY_FILE_PATH, 'a') as file:
				file.write(f"{form.cleaned_data['text']} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
			return (redirect('form'))
	else:
		form = theForm()
		if os.path.exists(settings.HISTORY_FILE_PATH):
			with open(settings.HISTORY_FILE_PATH, 'r') as file:
				history = file.readlines()
		else:
			history = []
		history = [line.strip() for line in history]
		context = {
			'form' : form,
			'history' : history,
		}
	return render(request,'ex02/form.html',context)
	