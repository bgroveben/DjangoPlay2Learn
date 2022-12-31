import json

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, UpdateView
# from django.views.generic import (
#    CreateView, DeleteView, DetailView, ListView, UpdateView
#)
from .forms import CustomUserChangeForm, ReviewForm
from .models import CustomUser, Review




class MyAccountPageView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    success_message = 'Update Successful'
    template_name = 'account/my_account.html'
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user


class ReviewView(FormView):
    # https://stackoverflow.com/questions/59638245/how-do-i-call-a-function-when-i-make-a-post-request-at-python
    template_name = 'users/reviews.html'
    form_class = ReviewForm
    success_url = reverse_lazy('users:reviewspage')
    #record_review(request)
    #vote(request)


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
def record_review(request):
    data = json.loads(request.body)
    vote = data['vote']
    game = data['game']
    comment = data['comment']
    customuser = data['customuser']
    created = data['created']
    updated = data['updated']
    review = Reviews(vote=vote, game=game, comment=comment, customuser=customuser, created=created, updated=updated)
    review.save()
    # response = {"success": True}
    #response = {
        #'comment': comment,
        #'customuser': customuser
    #}
    #return JsonResponse(response)
    return JsonResponse(review)


#def vote(request, slug):
def vote(request):
    customuser = request.customuser # The logged-in user (or AnonymousUser).
    #review = review.objects.get(slug=slug) # The review instance.
    data = json.loads(request.body) # Data from the JavaScript.

    # Set simple variables.
    vote = data['vote'] # The user's new vote.
    likes = data['likes'] # The number of likes currently displayed on page.
    dislikes = data['dislikes'] # The number of dislikes currently displayed.

    if user.is_anonymous: # User not logged in. Can't vote.
        msg = 'Sorry, you have to be logged in to vote.'
    else: # User is logged in.
        if Review.objects.filter(customuseruser=customuser, review=review).exists():
            # User already voted. Get user's past vote:
            review = Review.objects.get(user=user, review=review)

            if review.vote == vote: # User's new vote is the same as old vote.
                msg = 'Right. You told us already. Geez.'
            else: # User changed vote.
                review.vote = vote # Update Review instance.
                review.save() # Save.

                # Set data to return to the browser.
                if vote == -1:
                    likes -= 1
                    dislikes += 1
                    msg = "Don't like it after all, huh? OK. Noted."
                else:
                    likes += 1
                    dislikes -= 1
                    msg = 'Grown on you, has it? OK. Noted.'
        else: # First time user is voting on this review.
            # Create and save new vote.
            review = Review(user=user, review=review, vote=vote)
            review.save()

            # Set data to return to the browser.
            if vote == -1:
                dislikes += 1
                msg = "Sorry you didn't like the review."
            else:
                likes += 1
                msg = "Yeah, good one, right?"

    # Create object to return to browser.
    response = {
        'msg': msg,
        'likes': likes,
        'dislikes': dislikes
    }
    return JsonResponse(response) # Return object as JSON.




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
