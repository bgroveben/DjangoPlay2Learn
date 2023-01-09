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
from .forms import CustomUserChangeForm, ReviewForm
from .models import CustomUser, ReviewModel, ReviewVote


"""
# https://www.youtube.com/watch?v=reFJ9hBLFUY
def Review_rate(request):
    if request.method == 'GET':
        comment = request.GET.get('comment')
        ...
        review = Reviews(vote=vote, game=game, comment=comment, customuser=customuser, created=created, updated=updated)
        review.save()
        return redirect('?', x=x)
"""

# Each view is responsible for doing one of two things: Returning an HttpResponse object containing the content for the requested page, or raising an exception such as Http404. The rest is up to you.
# https://docs.djangoproject.com/en/4.1/intro/tutorial03/#write-views-that-actually-do-something


class MyAccountPageView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = get_user_model()
    # model = CustomUser
    form_class = CustomUserChangeForm
    success_message = 'Update Successful'
    template_name = 'account/my_account.html'
    # AFTER UPDATE is clicked: Exceptioon
    # Reverse for 'my_account' not found. 'my_account' is not a valid view function or pattern name.
    success_url = reverse_lazy('users:my_account')

    def get_object(self):
        return self.request.user


#def my_reviews(request):
    #review = Reviews.objects.all()
    #review = Review.objects.all().order_by('-created')
    #return render(request, 'user/reviews.html',{'reviews':reviews})
    #return render(request,
                #'user/reviewspage.html'
                #{'reviewspage':reviewspage}
                #)
"""
https://www.youtube.com/watch?v=1ihn3iRXtsY  11:23
def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # assert False
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'pages/contact.html', { 'form': form, 'page_list': Page.objects.all(), 'submitted': submitted })
"""

#def vote(request, slug): replace slug with url?
def vote(request, slug):
    customuser = request.customuser # The logged-in user (or AnonymousUser).
    review = review.objects.get(slug=slug) # The review instance.
    data = json.loads(request.body) # Data from the JavaScript.

    # Set simple variables.
    vote = data['vote'] # The user's new vote.
    likes = data['likes'] # The number of likes currently displayed on page.
    dislikes = data['dislikes'] # The number of dislikes currently displayed.

    if user.is_anonymous: # User not logged in. Can't vote.
        msg = 'Sorry, you have to be logged in to vote.'
    else: # User is logged in.
        if ReviewModel.objects.filter(customuseruser=customuser, review=review).exists():
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


class ReviewListView(ListView):
    model = ReviewModel



class ReviewView(FormView, SuccessMessageMixin, LoginRequiredMixin):
    # When I include UpdateView above:
    # => Generic detail view ReviewView must be called with either an object pk or a slug in the URLconf.
    # https://stackoverflow.com/questions/59638245/how-do-i-call-a-function-when-i-make-a-post-request-at-python
    model = ReviewModel
    template_name = 'users/reviews.html'
    success_message = 'Review Submitted'
    form_class = ReviewForm
    #success_url = reverse_lazy('users:reviewspage')
    success_url = reverse_lazy('users')
    #record_review(request)
    #vote(request)

    #def get_object(self):
        #return self.request.user


class ReviewsPageView(TemplateView):
    model = ReviewModel
    template_name = "users/reviewspage.html"

    def get_context_data(self, **kwargs):
        context = super(ReviewsPageView, self).get_context_data(**kwargs)
        context['reviews'] = ReviewModel.objects.all().order_by('-created')
        #context['reviews'] = Review.objects.filter('-created')
        #context['anagram_scores'] = GameScores.objects.filter(game__exact='ANAGRAM').order_by('-score')
        #context['math_scores'] = GameScores.objects.filter(game__exact='MATH').order_by('-score')
        #context['test'] = ['this is a test']
        return context


"""
https://realpython.com/django-social-post-3/#handle-post-requests-in-django-code-logic

def profile(request, pk):
    # pk = primary key
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "dwitter/profile.html", {"profile": profile})


from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})



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
