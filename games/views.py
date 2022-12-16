import json
from django.http import JsonResponse

# from django.shortcuts import render
from django.views.generic import TemplateView

from .models import GameScores

def record_score(request):
    data = json.loads(request.body)
    username = data["username"]
    game = data["game"]
    score = data["score"]
    new_score = GameScores(username=username, game=game, score=score)
    new_score.save()
    response = {"success": True}
    return JsonResponse(response)


class HomeView(TemplateView):
    template_name = "home.html"


class GamesView(TemplateView):
    template_name = "games.html"


class GameScoresView(TemplateView):
    template_name = "game-scores.html"

    def get_context_data(self, **kwargs):
        context = super(GameScoresView, self).get_context_data(**kwargs)
        context['game_scores'] = GameScores.objects.all()
        context['anagram_scores'] = GameScores.objects.filter(game__exact='ANAGRAM').order_by('-score')
        context['math_scores'] = GameScores.objects.filter(game__exact='MATH').order_by('-score')
        context['test'] = ['this is a test']
        return context
