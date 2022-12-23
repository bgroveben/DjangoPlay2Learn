#from django.shortcuts import render # Do I need this?

# Create your views here.
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .forms import CustomUserChangeForm
#from django.views.generic import (
    #CreateView, UpdateView, FormView, TemplateView
    #)
#from django.views.generic import (
    #CreateView, DeleteView, DetailView, ListView, UpdateView
#)

# from allauth.account.decorators import verified_email_required
#from allauth.account.views import PasswordChangeView, LoginView, LogoutView

#from .forms import CustomUserChangeForm
#from allauth.account.forms import LoginForm

class MyAccountPageView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    success_message = 'Update Successful'
    template_name = 'account/my_account.html'
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user

# https://www.youtube.com/watch?v=BiHSP6bTsrE&list=PLLRM7ROnmA9GTk309hETb92m_XN7HHiSJ&index=2  ~20:00 Create register view


#class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    #success_url = reverse_lazy('my-account')


#class SignupPageView(FormView, SuccessMessageMixin):
#class SignupPageView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    #success_url = reverse_lazy('games:homepage')
    #model = get_user_model()
    #form_class = CustomSignupForm
    #success_message = 'Thank you for registering'
    #template_name = "account/signup.html"

    #def get_object(self):
        #return self.request.user

#class SignupPageView(TemplateView):
    #template_name = "account/signup.html"

#class LoginPageView(FormView, SuccessMessageMixin):
#class LoginPageView(TemplateView):
#class LoginPageView( FormView, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    #model = get_user_model
    #form_class = LoginForm
    #success_message = 'You are logged in'
    #template_name = 'account/login.html'
    #success_url = reverse_lazy('games:games')
    #template_name = 'games.html'
    #success_url = reverse_lazy('games')
    #https://stackoverflow.com/questions/6266415/django-class-based-generic-view-no-url-to-redirect-to
    #->CreateView.as_view(model=myModel, success_url=reverse('success-url'))

    #def get_object(self):
        #return self.request.user
