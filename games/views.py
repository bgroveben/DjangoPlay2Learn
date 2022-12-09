import json
from django.http import JsonResponse

from django.shortcuts import render
from django.views.generic import TemplateView


def record_score(request):
    data = json.loads(request.body)
    user_name = data["user-name"]
    game = data["game"]
    score = data["score"]
    new_score = GameScore(user_name=user_name, game=game, score=score)
    new_score.save()
    response = {"success": True}
    return JsonResponse(response)


class HomeView(TemplateView):
    template_name = "home.html"

class MathGameView(TemplateView):
    template_name = "math-game.html"

class AnagramGameView(TemplateView):
    template_name = "anagram-game.html"
