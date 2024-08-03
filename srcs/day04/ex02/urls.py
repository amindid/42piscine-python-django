from django.urls import path
from . import views

urlpatterns = [
	path('ex02', views.django_framework_web, name='Django_Framework_Web'),
]