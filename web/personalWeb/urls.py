from django.urls import path
from personalWeb import views

urlpatterns = [
	path('', views.home_page, name='home_page'),
]