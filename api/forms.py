from django import forms
from django.core.exceptions import ValidationError
from .models import  Contact    



class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'
    
    #name = forms.CharField(max_length=100, required=True)
    #email = forms.EmailField(required=True)
    #subject = forms.CharField(max_length=255, required=True)
    #message = forms.CharField(widget=forms.Textarea)

