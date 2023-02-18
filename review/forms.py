from .models import Review
from django import forms
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
        widgets = {
            'comment': forms.Textarea(attrs={'rows': '3'})
        }
