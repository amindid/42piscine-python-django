from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage, name='homepage'),
	path('login', views.login, name='login'),
	path('registration', views.registration, name='registration'),
	path('emailConfirmation', views.emailConfirmation, name='emailConfirmation'),
	path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]