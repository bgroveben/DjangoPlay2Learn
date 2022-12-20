from django.shortcuts import render # Do I need this?

# Create your views here.
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, FormView, TemplateView

from allauth.account.views import PasswordChangeView

from .forms import CustomUserChangeForm, SignupForm


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('my-account')

class MyAccountPageView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    success_message = 'Update Successful'
    template_name = 'account/my_account.html'

    def get_object(self):
        return self.request.user


class SignupPageView(FormView):
#class SignupPageView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = SignupForm
    template_name = "account/signup.html"

    def get_object(self):
        return self.request.user

#class SignupPageView(TemplateView):
    #template_name = "account/signup.html"

#class LoginPageView(FormView):
class LoginPageView(TemplateView):
    template_name = 'account/login.html'
