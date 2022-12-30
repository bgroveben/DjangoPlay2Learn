
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, UpdateView

from .forms import CustomUserChangeForm, ReviewForm
from users.models import Review


def record_review(request):
    data = json.loads(request.body)
    game = data['game']
    comment = data['comment']
    customuser = data['customuser']
    created = data['created']
    updated = data['updated']
    review = Reviews(game=game, comment=comment, customuser=customuser, created=created, updated=updated)
    review.save()
    response = {"success": True}
    return JsonResponse(response)


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
    success_url = reverse_lazy('users:reviewspage')


class ReviewsPageView(TemplateView):
    template_name = "users/reviewspage.html"

    def get_context_data(self, **kwargs):
        context = super(ReviewsPageView, self).get_context_data(**kwargs)
        context['reviews'] = Review.objects.all().order_by('-created')
        #context['anagram_scores'] = GameScores.objects.filter(game__exact='ANAGRAM').order_by('-score')
        #context['math_scores'] = GameScores.objects.filter(game__exact='MATH').order_by('-score')
        #context['test'] = ['this is a test']
        return context


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
