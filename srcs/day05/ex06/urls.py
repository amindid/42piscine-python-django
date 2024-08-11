from django.urls import path
from . import views

urlpatterns = [
	path('ex06/init', views.init_view, name='init_view'),
	path('ex06/populate', views.populate_view, name='populate_view'),
	path('ex06/display', views.display_view, name='display_view'),
	path('ex06/update', views.update_view, name='update_view'),
]