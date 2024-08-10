from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .models import Movies
import psycopg2
from psycopg2 import sql
from django.http import HttpResponse

# Create your views here.


def init_view(request):
	db_params = {
		'dbname' : settings.DATABASES['default']['NAME'],
		'user' : settings.DATABASES['default']['USER'],
		'password' : settings.DATABASES['default']['PASSWORD'],
		'host' : settings.DATABASES['default']['HOST'],
		'port' : settings.DATABASES['default']['PORT'],
	}
	try:
		#connect this django app with postgreSQL database
		connection = psycopg2.connect(**db_params)
		#creat a cursor that is the primary tool for executing SQL commands and queries
		cursor = connection.cursor()
		#postgreSQL command that will be executed by cursor to creat a table
		table_query = sql.SQL("""
			CREATE TABLE IF NOT EXISTS ex04_movies (
				title VARCHAR(64) NOT NULL UNIQUE,
				episode_nb BIGINT PRIMARY KEY,
				opening_crawl TEXT,
				director VARCHAR(32) NOT NULL,
				producer VARCHAR(128) NOT NULL,
				release_date DATE NOT NULL
			);

		""")
		# execute the table_query with cursor
		cursor.execute(table_query)
		# commit changes
		connection.commit()
		# close connection and cursor
		cursor.close()
		connection.close()
		return HttpResponse("OK")
	except Exception as e:
		return HttpResponse(f"ERROR: {e}")

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
		Movies.objects.bulk_create(records)
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
	return render(request, "ex04/index.html", context)

def remove_view(request):
	if request.method == "POST":
		films_list = request.POST.getlist('films')
		for film in films_list:
			movie = get_object_or_404(Movies, episode_nb=film)
			movie.delete()
		all_records = Movies.objects.all()
		context = {
			'records' : all_records,
		}
		return render(request, "ex04/index.html", context)
			
	else:
		if not Movies.objects.exists():
			return HttpResponse("No data available")
		all_records = Movies.objects.all()
		context = {
			'records' : all_records,
		}
		return render(request, "ex04/deleteForm.html", context)


# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# from .models import Movies

# def remove_view(request):
#     if request.method == "POST":
#         # Retrieve selected film episode numbers
#         films_list = request.POST.getlist('films')
        
#         for film in films_list:
#             # Remove each selected movie
#             movie = get_object_or_404(Movies, episode_nb=film)
#             movie.delete()

#         # Fetch updated list of records
#         all_records = Movies.objects.all()
#         context = {
#             'records': all_records,
#         }
#         return render(request, "ex04/index.html", context)
        
#     else:
#         # Check if there are any records available
#         if not Movies.objects.exists():
#             return HttpResponse("No data available")
        
#         # Fetch all records for the form
#         all_records = Movies.objects.all()
#         context = {
#             'records': all_records,
#         }
#         return render(request, "ex04/deleteForm.html", context)