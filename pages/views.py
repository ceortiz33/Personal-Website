from django.views.generic import View
from django.shortcuts import render
from github import Github

from project.models import Project

def home(request):
	"""The home page"""
	return render(request, "pages/home.html")

def  about(request):
	"""The about page of my portfolio"""
	return render(request,"pages/about.html")

def services(request):
	"""The services page of my portofolio"""
	return render(request,"pages/services.html")

def skills(request):
	"""The skills page of my portfolio"""
	return render(request,"pages/skills.html")

def projects(request):
	"""The teams page of my portfolio"""
	g = Github("token")
	for repo in g.get_user().get_repos():
		print(repo.name)

	return render(request,"pages/projects.html")

def contacts(request):
	"""The contacts page of my portfolio"""
	return render(request,"pages/contacts.html")