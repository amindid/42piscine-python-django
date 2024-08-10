from django.urls import path
from . import views

urlpatterns = [
	path('ex04/init', views.init_view, name='init_view'),
	path('ex04/populate', views.populate_view, name='populate_view'),
	path('ex04/display', views.display_view, name='display_view'),
	path('ex04/remove', views.remove_view, name='remove_view'),
]