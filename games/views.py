import json
from django.http import JsonResponse
from django.views.generic import TemplateView
#from django.shortcuts import get_object_or_404

from .models import GameScores


"""
# https://www.edureka.co/community/80838/how-to-get-the-currently-logged-in-user-s-user-id-in-django
def sample_view(request):
    current_user = request.user
    print current_user.id

if request.user.is_authenticated:
    # Do something for authenticated users.
else:
    # Do something for anonymous users.
"""

def record_score(request):
    """
    Get data from Vue via the recordScore function in the AH and MF components
    """
    data = json.loads(request.body)
    #username = data["username"] also works
    username = request.user
    score = data["score"]
    gamelength = data["gamelength"]
    maxnum = data["maxnum"]
    operation = data["operation"]
    game = data["game"]
    new_score = GameScores(username=username, game=game, score=score, maxnum=maxnum, gamelength=gamelength, operation=operation)
    new_score.save()
    response = {"success": True}
    return JsonResponse(response)


class HomeView(TemplateView):
    template_name = "home.html"


class GamesView(TemplateView):
    template_name = "games/games.html"


class GameScoresView(TemplateView):
    # template filters -> {{ value|filter:arg }}
    template_name = "games/game-scores.html"
    # https://docs.djangoproject.com/en/4.1/topics/class-based-views/generic-display/#viewing-subsets-of-objects:
    #context_object_name = 'username'
    #queryset = Publisher.objects.all()

    # https://stackoverflow.com/questions/36950416/when-to-use-get-get-queryset-get-context-data-in-django
    def get_context_data(self, **kwargs):
        context = super(GameScoresView, self).get_context_data(**kwargs)
        context['game_scores'] = GameScores.objects.all()
        context['anagram_scores'] = GameScores.objects.filter(game__exact='ANAGRAM').order_by('-score')
        context['math_scores'] = GameScores.objects.filter(game__exact='MATH').order_by('-score')
        context['allscores'] = GameScores.objects.all().order_by('-username')
        #context['myscores'] = GameScores.objects.filter(username='admin')
        #context['username'] = GameScores.objects.all().filter(username='admin')
        context['myscores'] = GameScores.objects.all().filter(username=self.request.user)
        #context['queryset'] = GameScores.objects.get_queryset()
        context['queryset'] = GameScores.objects.get_queryset().filter(username=self.request.user)

        #context['username'] = GameScores.objects.all().filter(username)
        #context['username'] = GameScores.objects.username
        #context['username'] = self.kwargs['score']
        #context['username'] = self.kwargs['pk']
        #context['username'] = self.kwargs['username']
        #context['data'] = self.kwargs.get({'kwargs':kwargs})
        #context['data'] = GameScores.get_context_data(**kwargs)
        #context['username'] = get_object_or_404(GameScores, username=self.kwargs.get('username'))

        #context['myscores'] = GameScores.objects.filter(username=str(GameScores.username))
        #context['myscores'] = GameScores.username
        #context['myscores'] = GameScores.objects.filter(username__exact=GameScores.username)
        #context['myscores'] = GameScores.objects.filter(username__exact=GameScores.username).order_by('-score')
        #context['test'] = ['this is a test']
        #context['myscores'] = GameScores.objects.filter(username__exact=request.user)
        #context['myscores'] = GameScores.objects.filter(username__exact=GameScores.username).order_by('-score')
        return context


class MyScoresView(TemplateView):
    # template filters -> {{ value|filter:arg }}
    template_name = "games/myscores.html"

    def get_context_data(self, **kwargs):
        context = super(MyScoresView, self).get_context_data(**kwargs)
        context['game_scores'] = GameScores.objects.all()
        context['myscores'] = GameScores.objects.filter(username='admin')
        #context['myscores'] = #GameScores.objects.filter(username__exact=request.user)
        #context['myscores'] = GameScores.objects.filter()
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
