
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView

from .forms import CustomUserChangeForm, ReviewForm

class MyAccountPageView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    success_message = 'Update Successful'
    template_name = 'account/my_account.html'
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user


class ReviewView(FormView):
    template_name = 'users/reviews.html'
    form_class = ReviewForm
    success_url = reverse_lazy('users:reviews')
"""
https://blog.devgenius.io/lets-build-a-movie-review-django-app-47658f8e3751

from django.shortcuts import render,redirect
from . models import Movie
from . models import Review
from . forms import ReviewForm


def home(request):
    items = Movie.objects.all()
    context = {
        'items':items
    }
    return render(request, "movie/home.html",context)
"""
