"""Defines URL patterns for pages """
from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
	#Page that show home page
	path('',views.home, name='home'),
	path('home/', views.home, name='home'),
	#Page that show about section.
	path('about/', views.about, name='about'),
	#Page that show services section
	path('services/',views.services, name='services'),
	#Page that show skills section
	path('skills/',views.skills, name='skills'),
	#Page that show teams section
	path('teams/',views.teams, name='teams'),
	#Page that show contacts section
	path('contacts/',views.contacts, name='contacts'),
]