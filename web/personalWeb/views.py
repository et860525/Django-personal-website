from django.http import request
from django.shortcuts import render

# Create your views here.
def home_page(request):
	return render(request, 'home.html')

def project_page(request):
	return render(request, 'project.html')

def blog_page(request):
	pass

def contact_page(request):
	pass

def about_page(request):
	pass