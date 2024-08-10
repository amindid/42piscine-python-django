from django.urls import path
from . import views

urlpatterns = [
	path('ex03/populate', views.populate_view, name='populate_view'),
	path('ex03/display', views.display_view, name='display_view'),
]