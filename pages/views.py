from django.views.generic import View
from django.shortcuts import render

def home(request):
	"""The home page"""
	return render(request, "pages/base.html")

def  about(request):
	"""The about page of my portfolio"""
	return render(request,"pages/about.html")

def services(request):
	"""The services page of my portofolio"""
	return render(request,"pages/services.html")

def skills(request):
	"""The skills page of my portfolio"""
	return render(request,"pages/skills.html")

def teams(request):
	"""The teams page of my portfolio"""
	return render(request,"pages/teams.html")

def contacts(request):
	"""The contacts page of my portfolio"""
	return render(request,"pages/contacts.html")