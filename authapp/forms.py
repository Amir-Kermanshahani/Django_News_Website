from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

# from .models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegistrationForm(forms.ModelForm):

    class Meta:
        model = User    
        fields = [
    		    'username', 
    		    'password', 
    		    'email'
    	]   
