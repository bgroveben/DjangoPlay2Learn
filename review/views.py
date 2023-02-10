from django.views.generic import TemplateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import Review
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


class MyReviewsView(SuccessMessageMixin, TemplateView):
    # template filters -> {{ value|filter:arg }}
    template_name = "review/myreviews.html"

    def get_context_data(self, **kwargs):
        context = super(MyReviewsView, self).get_context_data(**kwargs)
        context['reviews'] = Review.objects.all()
        context['anagram_reviews'] = Review.objects.filter(game__exact='ANAGRAM HUNT').order_by('-votes')
        context['math_reviews'] = Review.objects.filter(game__exact='MATH FACTS').order_by('-votes')
        context['allreviews'] = Review.objects.all().order_by('-username')
        context['myreviews'] = Review.objects.all().filter(username=self.request.user)
        return context


class ReviewDeleteView(DeleteView):
    model = Review
    success_url = '/review/myreviews/'

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Review deleted.')
        return result

    def test_func(self):
        # This is a hack. Check your tests file.
        #obj = self.get_object()
        #return self.request.user == obj.user
        return True

