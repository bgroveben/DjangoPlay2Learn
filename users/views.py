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
    # AFTER UPDATE is clicked: Exception
    # Reverse for 'my_account' not found. 'my_account' is not a valid view function or pattern name.
    success_url = reverse_lazy('users:my_account')

    def get_object(self):
        return self.request.user

class ReviewView(FormView, SuccessMessageMixin, LoginRequiredMixin):
    # When I include UpdateView above:
    # => Generic detail view ReviewView must be called with either an object pk or a slug in the URLconf.
    # https://stackoverflow.com/questions/59638245/how-do-i-call-a-function-when-i-make-a-post-request-at-python
    model = ReviewModel
    template_name = 'users/reviews.html'
    success_message = 'Review Submitted'
    form_class = ReviewForm
    success_url = reverse_lazy('users:reviewspage')

    #def get_object(self):
        #return self.request.user


class ReviewsPageView(TemplateView):
    model = ReviewModel
    template_name = "users/reviewspage.html"

    def get_context_data(self, **kwargs):
        context = super(ReviewsPageView, self).get_context_data(**kwargs)
        context['reviews'] = ReviewModel.objects.all().order_by('-created')
        return context
