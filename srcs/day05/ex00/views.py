from django.shortcuts import render
from django.conf import settings
import psycopg2
from psycopg2 import sql
from django.http import HttpResponse
# Create your views here.
def my_view(request):
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
			CREATE TABLE IF NOT EXISTS ex00_movies (
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