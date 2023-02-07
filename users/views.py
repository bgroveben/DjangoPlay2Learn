import json

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, UpdateView, ListView
# from django.views.generic import (
#    CreateView, DeleteView, DetailView, ListView, UpdateView
#)
from .forms import CustomUserChangeForm#, ReviewForm
from .models import CustomUser#, ReviewModel


# Each view is responsible for doing one of two things: Returning an HttpResponse object containing the content for the requested page, or raising an exception such as Http404. The rest is up to you.
# https://docs.djangoproject.com/en/4.1/intro/tutorial03/#write-views-that-actually-do-something


class MyAccountPageView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = get_user_model()
    # model = CustomUser
    form_class = CustomUserChangeForm
    success_message = 'Update Successful'
    template_name = 'account/my_account.html'
    # AFTER UPDATE is clicked: Exception
    # Reverse for 'my_account' not found. 'my_account' is not a valid view function or pattern name.
    success_url = reverse_lazy('users:my_account')

    def get_object(self):
        return self.request.user
