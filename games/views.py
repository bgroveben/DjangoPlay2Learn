import json
from django.http import JsonResponse
from django.views.generic import TemplateView

from .models import GameScores


def record_score(request):
    """
    Get data from Vue via the recordScore function in the AH and MF components
    """
    data = json.loads(request.body)
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
    template_name = "games/game-scores.html"

    def get_context_data(self, **kwargs):
        context = super(GameScoresView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScores.objects.filter(game__exact='ANAGRAM').order_by('-score')
        context['math_scores'] = GameScores.objects.filter(game__exact='MATH').order_by('-score')
        return context


class MyScoresView(TemplateView):
    # template filters -> {{ value|filter:arg }}
    template_name = "games/myscores.html"

    def get_context_data(self, **kwargs):
        context = super(MyScoresView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScores.objects.filter(game__exact='ANAGRAM').order_by('-score')
        context['math_scores'] = GameScores.objects.filter(game__exact='MATH').order_by('-score')
        context['allscores'] = GameScores.objects.all().order_by('-username')
        context['myscores'] = GameScores.objects.all().filter(username=self.request.user)
        return context
