from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def home_page(request):
	return render(request, 'personalWeb/home.html')

def project_page(request):
	return render(request, 'personalWeb/project.html')

def contact_page(request):
	form = ContactForm()

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			pass
		
		return redirect("home_page")

	return render(request, 'personalWeb/contact.html', {'form': form})

def about_page(request):
	return render(request, 'personalWeb/about.html')