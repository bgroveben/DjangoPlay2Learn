from .models import Review
from django import forms
#from django.forms import TextInput


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ["game","votes","comment"]
        #fields = '__all__'
        widgets = {
            #'username': TextInput(attrs={'readonly': 'readonly'})
            'comment': forms.Textarea(attrs={'rows': '3'})
        }
