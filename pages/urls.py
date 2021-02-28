"""Defines URL patterns for pages """
from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
	#Page that show home page
	path('',views.home, name='home'),
	#Page that show about section.
	path('about/', views.about, name='about'),
]