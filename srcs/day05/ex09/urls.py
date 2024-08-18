from django.urls import path
from . import views

urlpatterns = [
	path('ex09/display', views.display_view, name='display_view'),
]