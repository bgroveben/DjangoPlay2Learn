from datetime import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

from users.models import ReviewModel


BIRTH_YEAR_CHOICES = range(1900, datetime.now().year)


class CustomUserChangeForm(UserChangeForm):
    # Do I need this just to add 'dob' and 'avatar'?
    password = None

    class Meta:
        model = get_user_model()
        fields = (
            'email', 'username', 'first_name', 'last_name', 'dob', 'avatar'
        )
        widgets = {
            'dob': forms.SelectDateWidget(
                attrs={
                    'style': 'width: 31%; display: inline-block; margin: 0 1%'
                },
                years = BIRTH_YEAR_CHOICES
            )
        }



class ReviewForm(forms.ModelForm):

    class Meta:
        model = ReviewModel
        fields = ['game', 'comment']

    game = forms.CharField()
    comment = forms.CharField(max_length=200)
    #vote = forms.IntegerField()
    #customuser = forms.CharField() # username
    customuser = ReviewModel.customuser
    created = ReviewModel.created
    updated = ReviewModel.updated
    #created = forms.DateTimeField()
    #updated = forms.DateTimeField()
    #rating = forms.?


"""
from users.models import Review
from django import forms


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ["author","stars","comment"]
"""
