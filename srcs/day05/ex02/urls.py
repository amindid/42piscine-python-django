from django.urls import path
from . import views

urlpatterns = [
	path('ex02/init', views.init_view, name='init_view')
	path('ex02/populate', views.populate_view, name='populate_view')
	path('ex02/display', views.display_view, name='display_view')
]