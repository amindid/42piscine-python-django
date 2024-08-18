"""
URL configuration for day05 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ex00.urls')),
    path('', include('ex02.urls')),
    path('', include('ex03.urls')),
    path('', include('ex04.urls')),
    path('', include('ex05.urls')),
    path('', include('ex06.urls')),
    path('', include('ex07.urls')),
    path('', include('ex08.urls')),
    path('', include('ex09.urls')),
]
