from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the review index.")


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
