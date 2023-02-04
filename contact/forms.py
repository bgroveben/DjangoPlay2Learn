from django import forms
from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            #'username': TextInput(attrs={'readonly': 'readonly'})
            'message': forms.Textarea(attrs={'rows': '3'})
        }
