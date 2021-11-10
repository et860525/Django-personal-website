from django import forms

from .models import Task

class DateInput(forms.DateInput):
    input_type = 'date'

class CreateTaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['name', 'detail', 'due_date']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
			'detail': forms.TextInput(attrs={'class': 'form-control mb-3'}),
			'due_date': DateInput(attrs={'class': 'form-control mb-3'}),
		}

class UpdateTaskForm(forms.Form):
	pk = forms.IntegerField(label='',widget=forms.NumberInput(attrs={'style': 'display: none;'}),required=False)
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
	detail = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3'}), required=False)
	due_date = forms.DateField(widget=DateInput(attrs={'class': 'form-control mb-3'}))