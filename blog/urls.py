from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
	path('', views.home_page, name='home_page'),
]