from django.shortcuts import render
from .models import People, Planets, Movies
from django.http import HttpResponse
from django.conf import settings
import psycopg2
from psycopg2 import sql
from datetime import datetime
# Create your views here.

def main_view(request):
	if request.method == "GET":
		genders = People.objects.values_list('gender', flat=True).distinct()
		context = {
			'genders' : genders,
		}
		return render(request, 'ex10/form.html', context)
	if request.method == "POST":
		max_date_str = request.POST.get('max_release_date')
		min_date_str = request.POST.get('min_release_date')
		max_date = datetime.strptime(max_date_str, '%Y-%m-%d').date() if max_date_str else None
		min_date = datetime.strptime(min_date_str, '%Y-%m-%d').date() if min_date_str else None
		character_gender = request.POST.get('character_gender')
		planet_diameter = request.POST.get('planet_diameter')
		characters = People.objects.filter(gender=character_gender).filter(homeworld__diameter__gte=planet_diameter)
		founded = []
		for movie in Movies.objects.all():
			if movie.release_date <= max_date and movie.release_date >= min_date:
				for char in characters:
					if char in movie.characters.all():
						founded.append((char, movie))
		if not founded:
			return HttpResponse("NO DATA")
		context = {
			'founded' : founded,
		}
		return render(request, 'ex10/index.html', context)
			
