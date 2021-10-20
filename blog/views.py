from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_page(request):
	return render(request, 'blog/home.html')

def post_page(request, post_headline):
	return render(request, 'blog/post.html', {'headline': post_headline})

@login_required
def post_add(request):
	return render(request, 'blog/post_form.html')

@login_required
def dashboard(request):
	return render(request, 'blog/auth_dashboard.html')