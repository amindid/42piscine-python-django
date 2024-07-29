from django.urls import path
from . import views

urlpatterns = [
	path('ex00/', views.markdown_cheatsheet, name='Markdown_Cheatsheet')
]