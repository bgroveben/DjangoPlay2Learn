from datetime import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
# from django.contrib.auth import authenticate

from allauth.account.forms import SignupForm


BIRTH_YEAR_CHOICES = range(1915, datetime.now().year)

"""
#class SignupForm(forms.Form):
class CustomSignupForm(SignupForm):
    #first_name = forms.CharField(max_length=50, required=False, label="First Name")
    #last_name = forms.CharField(max_length=50, required=False)
    username = forms.CharField(max_length=50)
    #email = forms.CharField(max_length=100)
    #password = forms.CharField(max_length=128)
    #repeat_password = forms.CharField(max_length=128)

    def signup(self, request, user):
        user = super(CustomSignupForm, self).save(request)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.password = self.cleaned_data['password']
        #user.repeat_password = self.cleaned_data['password']
        user.save()
"""

class CustomSignupForm(SignupForm):
    # https://gavinwiener.medium.com/modifying-django-allauth-forms-6eb19e77ef56
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['username'] = forms.CharField(required=True)
        #self.fields['password'] = forms.CharField(widget=forms.PasswordInput)

    def signup(self, request, user):
        username = self.cleaned_data.pop('username')
        # password = self.cleaned_data.get('password')
        user = super(CustomSignupForm, self).save(request)
        #user.username = self.cleaned_data['username']
        user.save()

"""
class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'] = forms.CharField(required=True)

    def login(self, request, user):
        username = self.cleaned_data.pop('username')
        user = super(CustomLoginForm, self).save(request)
        #user.username = self.cleaned_data['username']
        user.save()
        #return user

    #class Meta:
        #model = get_user_model()
        #fields = ('username', 'password')

"""
class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = get_user_model()
        fields = (
            'email', 'username', 'first_name', 'last_name', 'dob', 'avatar'
        )
        # fields = ['username', 'email', 'password', etc]
        #fields = ('email', 'username', 'first_name', 'last_name')

        widgets = {
            'dob': forms.SelectDateWidget( # Do I need dob?
                attrs={
                    'style': 'width: 31%; display: inline-block; margin: 0 1%'
                },
                years = BIRTH_YEAR_CHOICES
            )
        }
