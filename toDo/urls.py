from django.urls import path
from toDo import views

app_name = 'toDo'
urlpatterns = [
	path('', views.home_page, name='home_page'),
	path('create/', views.create_task, name='create_task_page'),
	path('delete/<int:pk>', views.delete_task, name='delete_task'),
]