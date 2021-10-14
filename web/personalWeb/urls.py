from django.urls import path
from personalWeb import views

urlpatterns = [
	path('', views.home_page, name='home_page'),
	path('project/', views.project_page, name='project_page'),
	path('blog/', views.blog_page, name='blog_page'),
	path('contact/', views.contact_page, name='contact_page'),
	path('about/', views.about_page, name='about_page')
]