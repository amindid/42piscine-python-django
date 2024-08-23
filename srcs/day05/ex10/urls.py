from django.urls import path
from . import views

urlpatterns = [
	path('ex10/', views.main_view, name='main_view')
]