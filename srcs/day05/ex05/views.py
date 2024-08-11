from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .models import Movies
import psycopg2
from psycopg2 import sql
from django.http import HttpResponse

# Create your views here.

def populate_view(request):
	try:
		records = [
			Movies(episode_nb=1,title="The Phantom Menace", director="George Lucas", producer="Rick McCallum", release_date="1999-05-09"),
			Movies(episode_nb=2,title="Attack of the Clones", director="George Lucas", producer="Rick McCallum", release_date="2002-05-16"),
			Movies(episode_nb=3,title="Revenge of the Sith", director="George Lucas", producer="Rick McCallum", release_date="2005-05-19"),
			Movies(episode_nb=4,title="A New Hope", director="George Lucas", producer="Gary Kurtz, Rick McCallum ", release_date="1977-05-25"),
			Movies(episode_nb=5,title="The Empire Strikes Back", director="Irvin Kershner", producer="Gary Kurtz, Rick McCallum", release_date="1980-05-17"),
			Movies(episode_nb=6,title="Return of the Jedi", director="Richard Marquand", producer="Howard G. Kazanjian, George Lucas, Rick McCallum", release_date="1983-05-25"),
			Movies(episode_nb=7,title="The Force Awakens", director="J. J. Abrams", producer="Kathleen Kennedy, J. J. Abrams, Bryan Burk", release_date="2015-12-11"),
		]
		for record in records:
			try:
				record.save()
			except Exception as e:
				continue
		return HttpResponse("OK")
	except Exception as e:
		return HttpResponse(f"ERROR : {e}")

def display_view(request):
	if not Movies.objects.exists():
		return HttpResponse("No data available")
	all_records = Movies.objects.all()
	context = {
		'records' : all_records,
	}
	return render(request, "ex05/index.html", context)

def remove_view(request):
	if request.method == "POST":
		films_list = request.POST.getlist('films')
		for film in films_list:
			movie = get_object_or_404(Movies, episode_nb=film)
			movie.delete()
		return redirect('remove_view')
			
	else:
		if not Movies.objects.exists():
			return HttpResponse("No data available")
		all_records = Movies.objects.all()
		context = {
			'records' : all_records,
		}
		return render(request, "ex05/deleteForm.html", context)