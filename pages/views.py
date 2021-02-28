from django.views.generic import View
from django.shortcuts import render

def home(request):
	"""The home page"""
	return render(request, "pages/base.html")

def  about(request):
	"""The about page of my portfolio"""
	return render(request,"pages/about.html")