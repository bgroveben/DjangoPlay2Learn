from .models import Review
from django import forms
#from django.forms import TextInput
from django.core.exceptions import ValidationError

def validate_form(form):
    if not form.is_valid():
        raise ValidationError(
            message='Please fill out all fields',
            code='invalid_form'
        )

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ["game","votes","comment"]
        #fields = '__all__'
        widgets = {
            #'username': TextInput(attrs={'readonly': 'readonly'})
            'comment': forms.Textarea(attrs={'rows': '3'})
        }
        #validators=[validate_form],
        #error_messages = {'invalid_form': 'Please fill out all fields'}
