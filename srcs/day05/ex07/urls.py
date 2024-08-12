from django.urls import path
from . import views

urlpatterns = [
	path('ex07/populate', views.populate_view, name='populate_view'),
	path('ex07/display', views.display_view, name='display_view'),
	path('ex07/update', views.update_view, name='update_view'),
]