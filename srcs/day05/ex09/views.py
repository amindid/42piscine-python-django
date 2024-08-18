from django.shortcuts import render
from .models import People, Planets
from django.http import HttpResponse
from django.conf import settings
import psycopg2
from psycopg2 import sql


def display_view(request):
	db_params = {
		'dbname' : settings.DATABASES['default']['NAME'],
		'user' : settings.DATABASES['default']['USER'],
		'password' : settings.DATABASES['default']['PASSWORD'],
		'host' : settings.DATABASES['default']['HOST'],
		'port' : settings.DATABASES['default']['PORT'],
	}
	connection = psycopg2.connect(**db_params)
	cursor = connection.cursor()
	table1_creation_query = sql.SQL("""
		CREATE TABLE IF NOT EXISTS ex09_planets (
			id SERIAL PRIMARY KEY,
			name VARCHAR(64) NOT NULL UNIQUE,
			climate VARCHAR(255),
			diameter INT,
			orbital_period INT,
			population BIGINT,
			rotation_period INT,
			surface_water REAL,
			terrain VARCHAR(128),
			created DATE NOT NULL,
			updated DATE NOT NULL
		);
	""")
	table2_creation_query = sql.SQL("""
		CREATE TABLE IF NOT EXISTS ex09_people (
			id SERIAL PRIMARY KEY,
			name VARCHAR(64) NOT NULL UNIQUE,
			birth_year VARCHAR(32),
			gender VARCHAR(32),
			eye_color VARCHAR(32),
			hair_color VARCHAR(32),
			height INT,
			mass REAL,
			homeworld INT,
			FOREIGN KEY (homeworld) REFERENCES "ex09_planets"(id),
			created DATE NOT NULL,
			updated DATE NOT NULL
		);
	""")
	cursor.execute(table1_creation_query)
	cursor.execute(table2_creation_query)
	connection.commit()
	cursor.close()
	connection.close()
	if not People.objects.exists():
		return HttpResponse("No data available, please use the following command line before use: python manage.py loaddata ex09_initial_data.json")
	characters = People.objects.all().order_by('name')
	planets = []
	for character in characters:
		try:
			planet = Planets.objects.get(id=character.homeworld)
		except Exception as e:
			planet = None
		planets.append(planet)
	context = {
		'characters' : characters,
		'planets' : planets
	}
	return render(request,'ex09/index.html',context)