from django.views.generic import View
from django.shortcuts import render
from github import Github
from .project import Project
import pandas as pd

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
	projects = []
	g = Github("29035651785d97e40f095706ad152b32c74da042")
	pj = { 'Title': [],
		   'Description': [],
		   'Language': [],
		   'Createdat':[],
		   'Size': [],
		   'Stars': [],
	}

	allProjects=[]
	for repo in g.get_user().get_repos():
		project = Project(repo.name, repo.description, repo.language, repo.created_at, repo.size, repo.stargazers_count)
		pj['Title'].append(project.title)
		pj['Description'].append(project.description)
		pj['Language'].append(project.language)
		pj['Createdat'].append(project.date_created)
		pj['Size'].append(project.size)
		pj['Stars'].append(project.stars)
	df = pd.DataFrame(pj, columns= ['Title', 'Description', 'Language', 'Createdat', 'Size', 'Stars'])
	print(df)
	for i in range(df.shape[0]):
		temp = df.loc[i]
		allProjects.append(dict(temp))
	context = {'allProjects': allProjects}
	return render(request,"pages/projects.html", context)

def contacts(request):
	"""The contacts page of my portfolio"""
	return render(request,"pages/contacts.html")