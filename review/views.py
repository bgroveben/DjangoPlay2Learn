import json
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import Review#, ReviewModel
from .forms import ReviewForm

@login_required
def index(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            sendreview = form.save(commit=False)
            # automagically get username for review
            sendreview.username = request.user
            sendreview.save()
            messages.success(request, 'Your review has been submitted')
            return redirect('review')
        else:
            return redirect('/')
    form = ReviewForm()
    context = {'form': form}
    return render(request, 'review/home.html', context)


def record_review(request):
    data = json.loads(request.body)
    game = data["game"]
    votes = data["votes"]
    comment = data["comment"]
    new_review = Review(username=request.user, game=game, votes=votes, comment=comment)
    new_review.save()
    response = {"success": True}
    return JsonResponse(response)


class ReviewView(SuccessMessageMixin, TemplateView):
    template_name = "review/reviews.html"
    form_class = ReviewForm
    success_message = 'Your review has been submitted'

    def get_context_data(self, **kwargs):
        context = super(ReviewView, self).get_context_data(**kwargs)
        context['reviews'] = Review.objects.all()
        context['anagram_reviews'] = Review.objects.filter(game__exact='ANAGRAM HUNT').order_by('-votes')
        context['math_reviews'] = Review.objects.filter(game__exact='MATH FACTS').order_by('-votes')
        return context

"""
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
"""

class ReviewsPageView(TemplateView):
    #model = ReviewModel
    model = Review
    template_name = "users/reviewspage.html"

    def get_context_data(self, **kwargs):
        context = super(ReviewsPageView, self).get_context_data(**kwargs)
        context['reviews'] = ReviewModel.objects.all().order_by('-created')
        return context
