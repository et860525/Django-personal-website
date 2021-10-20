from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
	path('', views.home_page, name='home_page'),
	path('dashboard/', views.dashboard, name='blog_dashboard_page'),
	path('post/<str:post_headline>/', views.post_page, name='post_page'),
	path('post/new/', views.post_add, name='new_post_page'),
]