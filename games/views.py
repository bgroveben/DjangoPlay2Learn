import json
from django.http import JsonResponse

# from django.shortcuts import render
from django.views.generic import TemplateView

from .models import GameScore

def record_score(request):
    data = json.loads(request.body)
    username = data["username"]
    game = data["game"]
    score = data["score"]
    new_score = GameScore(username=username, game=game, score=score)
    # new_score = GameScore(game=game, score=score)
    new_score.save()
    response = {"success": True}
    return JsonResponse(response)


class HomeView(TemplateView):
    template_name = "home.html"


class GamesView(TemplateView):
    template_name = "games.html"
