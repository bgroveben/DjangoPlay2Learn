from datetime import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm


BIRTH_YEAR_CHOICES = range(1900, datetime.now().year)


class CustomUserChangeForm(UserChangeForm):
    # Do I need this just to add 'dob'?
    password = None

    class Meta:
        model = get_user_model()
        fields = (
            'email', 'username', 'first_name', 'last_name', 'dob'
        )
        widgets = {
            'dob': forms.SelectDateWidget(
                attrs={
                    'style': 'width: 31%; display: inline-block; margin: 0 1%'
                },
                years = BIRTH_YEAR_CHOICES
            )
        }
