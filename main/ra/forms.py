from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User


		#fields = '__all__'

class CreateFolderForm(forms.ModelForm):
	class Meta:
		model = User_folder
		fields = ('folder_name',)

class LoginUser(UserCreationForm):
	class Meta:
		model = User
		fields = [ 'username', 'password' ]



		