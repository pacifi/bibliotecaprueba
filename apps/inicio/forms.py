from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
	"""docstring for UserForm"""
	telefono = forms.IntegerField()
	