from django.urls import path
from . import views

urlpatterns = [
	path('ex01/django', views.django_framework_web, name='Django_Framework_Web'),
	path('ex01/display', views.display_process, name='Display_Process'),
	path('ex01/templates', views.template_engine, name='Template_Engine'),
]