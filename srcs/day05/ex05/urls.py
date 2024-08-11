from django.urls import path
from . import views

urlpatterns = [
	path('ex05/populate', views.populate_view, name='populate_view'),
	path('ex05/display', views.display_view, name='display_view'),
	path('ex05/remove', views.remove_view, name='remove_view'),
]