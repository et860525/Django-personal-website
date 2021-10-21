from django import forms

class CreatePost(forms.Form):
	headline = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
	body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control mb-3'}))
	slug = forms.SlugField(help_text="Slug will automate create." ,widget=forms.TextInput(attrs={'class': 'form-control'}), required=None)
