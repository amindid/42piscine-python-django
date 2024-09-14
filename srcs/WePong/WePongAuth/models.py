from django.db import models
from django.utils import timezone
# Create your models here.

class Stats(models.Model):
	id = models.AutoField(primary_key=True)
	wins = models.IntegerField(default=0)
	losses = models.IntegerField(default=0)
	rank = models.CharField(max_length=255, default='Unranked')
	userId = models.OneToOneField('User', on_delete=models.CASCADE, unique=True)
	createdAt = models.DateTimeField(default=timezone.now)
	updatedAt = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.userId.username}'s Stats"



class User (models.Model):
	id = models.AutoField(primary_key=True)
	email = models.EmailField(unique=True)
	is_email_confirmed = models.BooleanField(default=False)
	username = models.CharField(max_length=255, unique=True)
	password = models.CharField(max_length=255)
	avatar = models.CharField(max_length=255, blank=True, null=True)
	isTwoFA = models.BooleanField(default=False)
	otpTwoFA = models.CharField(max_length=255, unique=True, blank=True, null=True)
	userStatus = models.CharField(max_length=255)
	userStatsId = models.OneToOneField('Stats', on_delete=models.SET_NULL, null=True, blank=True)
	Blocked = models.JSONField(default=list,blank=True)
	createdAt = models.DateTimeField(default=timezone.now)
	updatedAt = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.username
	
	def update_feilds(self, **kwargs):
		for field, value in kwargs.items():
			if hasattr(self, field):
				setattr(self, field, value)
		self.save()
	