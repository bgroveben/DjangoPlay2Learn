#import json
#import unittest
from django.test import TestCase# , RequestFactory
#from django.test import Client
from django.urls import reverse_lazy

from datetime import datetime

from users.models import CustomUser
from .models import GameScores
from .views import record_score, HomeView, GamesView, GameScoresView, MyScoresView


class TemplatesTest(TestCase):
    # Make sure templates, views, and urls match up
    def test_uses_home_templates(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, '_base.html')
        # self.assertTemplateUsed(response, '_base_vue.html') => fail

    def test_uses_games_templates(self):
        response = self.client.get('/games/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'games/games.html')
        self.assertTemplateUsed(response, '_base.html')
        self.assertTemplateUsed(response, '_base_vue.html')

    def test_uses_game_scores_templates(self):
        response = self.client.get('/game-scores/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'games/game-scores.html')
        self.assertTemplateUsed(response, '_base.html')
        #self.assertTemplateUsed(response, '_base_vue.html') => fail

    def test_uses_myscores_templates(self):
        response = self.client.get('/myscores/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'games/myscores.html')
        self.assertTemplateUsed(response, '_base.html')
        #self.assertTemplateUsed(response, '_base_vue.html') => fail

"""
class RecordGameScoresTest(TestCase):

    def test_can_save_POST_request(self):
        newscore = GameScores(username='admin', game='MATH', score=10, maxnum='50', gamelength='30', operation='+')
        scoresdict = {'username':'admin', 'game':'MATH', 'score':10, 'maxnum':'50', 'gamelength':'30', 'operation':'+'}
        gamescoresdict = GameScores(scoresdict)
        #response = self.client.post('record_score', data=new_score)
        response = self.client.post(reverse_lazy('games:record-score'), data=gamescoresdict)
        print(newscore)
"""
