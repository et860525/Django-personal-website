from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist

from .models import Task
from .forms import CreateTaskForm, UpdateTaskForm

# Create your views here.
def home_page(request):
	tasks = Task.objects.all()
	form = UpdateTaskForm()

	if request.method == 'POST':
		form = UpdateTaskForm(request.POST)
		if form.is_valid():
			try:
				task = Task.objects.get(id=form.cleaned_data['pk'])
				task.name = form.cleaned_data['name']
				task.detail = form.cleaned_data['detail']
				task.due_date = form.cleaned_data['due_date']
				task.save()
			except ObjectDoesNotExist:
				pass
		return redirect("toDo:home_page")

	return render(request, 'toDo/home.html', {'tasks': tasks, 'form': form})

def create_task(request):
	form = CreateTaskForm()

	if request.method == 'POST':
		form = CreateTaskForm(request.POST)

		if form.is_valid():
			form.save()
		return redirect("toDo:home_page")
			

	return render(request, 'toDo/task_form.html', {'form': form})

def delete_task(request, pk):
	task = Task.objects.get(id=pk)

	if request.method == 'POST':
		task.delete()
		return redirect('toDo:home_page')

	return render(request, 'toDo/delete_task.html', {'task': task})