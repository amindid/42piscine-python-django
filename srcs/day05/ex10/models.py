from django.db import models

# Create your models here.
class Planets(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=64, unique=True, null=False)
	climate = models.CharField(max_length=255, null=True)
	diameter = models.IntegerField(null=True)
	orbital_period = models.IntegerField(null=True)
	population = models.BigIntegerField(null=True)
	rotation_period = models.IntegerField(null=True)
	surface_water = models.FloatField(null=True)
	terrain = models.CharField(max_length=128, null=True)
	created = models.DateTimeField(auto_now_add=True,null=True)
	updated = models.DateTimeField(auto_now=True,null=True)
	
	def __str__(self):
		return self.name
	class Meta:
		db_table = 'ex10_planets'
	

class People(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=64, unique=True, null=False)
	birth_year = models.CharField(max_length=32, null=True)
	gender = models.CharField(max_length=32, null=True)
	eye_color = models.CharField(max_length=32, null=True)
	hair_color = models.CharField(max_length=32, null=True)
	height = models.IntegerField(null=True)
	mass = models.FloatField(null=True)
	created = models.DateTimeField(auto_now_add=True,null=True)
	updated = models.DateTimeField(auto_now=True,null=True)
	homeworld = models.ForeignKey(
		'Planets',
		to_field='id',
		null=True,
		on_delete=models.SET_NULL,
		db_column='homeworld',
	)

	def __str__(self):
		return self.name
	class Meta:
		db_table = 'ex10_people'

class Movies(models.Model):
	title = models.CharField(max_length=64, unique=True, null=False)
	episode_nb = models.IntegerField(primary_key=True)
	opening_crawl = models.TextField(null=True)
	release_date = models.DateField(null=False)
	director = models.CharField(max_length=32, null=False)
	producer = models.CharField(max_length=128, null=False)
	characters = models.ManyToManyField('People', related_name='movies')
	
	def __str__(self):
		return self.title
	class Meta:
		db_table = 'ex10_movies'