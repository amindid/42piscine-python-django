from django.db import models

# Create your models here.


# class User(models.Model):
# 	username= models.CharField(max_length=128, primary_key=True, null=False)
# 	password= models.CharField(max_length=128, null=False)
# 	def __str__(self):
# 		return self.username

class Tip(models.Model):
	content = models.TextField(max_length=128)
	author = fo