from django.urls import path
from . import views

urlpatterns = [
	path('ex03/', views.my_view, name='my_view'),
]