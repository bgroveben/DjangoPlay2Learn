import json
from django.http import JsonResponse
from django.views.generic import TemplateView

from .models import Review

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the review index.")


def record_review(request):
    data = json.loads(request.body)
    username = data["username"]
    game = data["game"]
    votes = data["votes"]
    comment = data["comment"]
    new_review = Review(username=username, game=game, votes=votes, comment=comment)
    new_review.save()
    response = {"success": True}
    return JsonResponse(response)


class ReviewView(TemplateView):
    template_name = "review/reviews.html"

    def get_context_data(self, **kwargs):
        context = super(ReviewView, self).get_context_data(**kwargs)
        context['reviews'] = Review.objects.all()
        context['anagram_reviews'] = Review.objects.filter(game__exact='ANAGRAM').order_by('-votes')
        context['math_reviews'] = Review.objects.filter(game__exact='MATH').order_by('-votes')
        return context

"""
from django.shortcuts import render,redirect
from . models import Game
from . models import Review
from . forms import ReviewForm


def home(request):
    items = Game.objects.all()
    context = {
        'items':items
    }
    return render(request, "review/home.html",context)


def rate(request, id):
    post = Game.objects.get(id=id)
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        author = request.POST.get('author')
        stars = request.POST.get('stars')
        comment = request.POST.get('comment')
        review = Review(author=author, stars = stars,  comment=comment , movie=post)
        review.save()
        return redirect('review:success')

    form = ReviewForm()
    context = {
        "form":form

    }
    return render(request, 'review/rate.html',context)


def success(request):
    return render(request, "review/success.html")
"""
