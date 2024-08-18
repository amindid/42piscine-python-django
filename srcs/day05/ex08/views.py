from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .models import People, Planets
import psycopg2
from psycopg2 import sql
from django.http import HttpResponse
import csv


def init_view(request):
	db_params = {
		'dbname' : settings.DATABASES['default']['NAME'],
		'user' : settings.DATABASES['default']['USER'],
		'password' : settings.DATABASES['default']['PASSWORD'],
		'host' : settings.DATABASES['default']['HOST'],
		'port' : settings.DATABASES['default']['PORT'],
	}
	try:
		connection = psycopg2.connect(**db_params)
		cursor = connection.cursor()
		table1_creation_query = sql.SQL("""
			CREATE TABLE IF NOT EXISTS ex08_planets (
				id SERIAL PRIMARY KEY,
				name VARCHAR(64) NOT NULL UNIQUE,
				climate VARCHAR(255),
				diameter INT,
				orbital_period INT,
				population BIGINT,
				rotation_period INT,
				surface_water REAL,
				terrain VARCHAR(128)
			);
		""")
		table2_creation_query = sql.SQL("""
			CREATE TABLE IF NOT EXISTS ex08_people (
				id SERIAL PRIMARY KEY,
				name VARCHAR(64) NOT NULL UNIQUE,
				birth_year VARCHAR(32),
				gender VARCHAR(32),
				eye_color VARCHAR(32),
				hair_color VARCHAR(32),
				height INT,
				mass REAL,
				homeworld VARCHAR(64),
				FOREIGN KEY (homeworld) REFERENCES "ex08_planets"(name)
			);
		""")
		cursor.execute(table1_creation_query)
		cursor.execute(table2_creation_query)
		connection.commit()
		cursor.close()
		connection.close()
		return HttpResponse("OK")
	except Exception as e:
		return HttpResponse(f"ERROR: {e}")
	
def populate_planets():
	with open('/Users/aouchaad/Desktop/42piscine-python-django/srcs/day05/ex08/planets.csv', 'r') as file:
		data = csv.reader(file, delimiter='\t')
		for row in data:
			planet = Planets()
			planet.name = row[0]
			planet.climate = row[1] or None
			planet.diameter = int(row[2]) if row[2] and row[2] != 'NULL' else None
			planet.orbital_period = int(row[3]) if row[3] and row[3] != 'NULL' else None
			planet.population = int(row[4]) if row[4] and row[4] != 'NULL' else None
			planet.rotation_period = int(row[5]) if row[5] and row[5] != 'NULL' else None
			planet.surface_water = float(row[6]) if row[6] and row[6] != 'NULL' else None
			planet.terrain = row[7] or None
			try:
				planet.save()
			except Exception as e:
				continue
		file.close()

def populate_people():
	with open('/Users/aouchaad/Desktop/42piscine-python-django/srcs/day05/ex08/people.csv', 'r') as file:
		data = csv.reader(file, delimiter='\t')
		for row in data:
			people = People()
			people.name = row[0] or None
			people.birth_year = row[1] or None
			people.gender = row[2] or None
			people.eye_color = row[3] or None
			people.hair_color = row[4] or None
			people.height = int(row[5]) if row[5] and row[5] != 'NULL' else None
			people.mass = float(row[6]) if row[6] and row[6] != 'NULL' else None
			homeworld_name = row[7] or None
			try:
				people.homeworld = Planets.objects.get(name=homeworld_name)
			except Exception as e:
				people.homeworld = None
			people.save()
		file.close()

def populate_view(request):
	try:
		populate_planets()
		populate_people()
		return HttpResponse("OK")
	except Exception as e:
		return HttpResponse(f"ERROR : {e}")

def display_view(request):
	if not People.objects.exists():
		return HttpResponse("No data available")
	characters = People.objects.all().order_by('name')
	planets = []
	for character in characters:
		try:
			planet = Planets.objects.get(name=character.homeworld)
		except Exception as e:
			planet = None
		planets.append(planet)
	context = {
		'characters' : characters,
		'planets' : planets
	}
	return render(request,'ex08/index.html',context)
