from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(label="Name:", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
	email = forms.EmailField(label="Email:", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
	message = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":30, 'class': 'form-control'}))