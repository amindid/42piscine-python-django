from django.db import models

# Create your models here.
class Planet(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=64, unique=True, null=False)
	climate = models.CharField(max_length=255, null=True)
	diameter = models.IntegerField(null=True)
	orbital_period = models.IntegerField(null=True)
	population = models.IntegerField(null=True)
	rotation_period = models.IntegerField(null=True)
	surface_water = models.FloatField(null=True)
	terrain = models.CharField(max_length=128, null=True)
	
	def __str__(self):
		return self.name
	

class People(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=64, unique=True, null=False)
	birth_year = models.CharField(max_length=32, null=True)
	gender = models.CharField(max_length=32, null=True)
	eye_color = models.CharField(max_length=32, null=True)
	hair_color = models.CharField(max_length=32, null=True)
	height = models.IntegerField(null=True)
	mass = models.FloatField(null=True)
	homeworld = models.ForeignKey(
		'Planet',
		to_field='name',
		null=True,
		on_delete=models.SET_NULL,
		db_column='homeworld',
		max_length=64
	)

	def __str__(self):
		return self.name