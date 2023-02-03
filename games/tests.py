import json
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


class GameScoresModelsTest(TestCase):

    def setUp(self):
        # Create test user
        testuser1 = CustomUser.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        testuser1.save()
        login = self.client.login(username=testuser1, password='1X<ISRUkw+tuK')

    def test_gamescores_model(self):
        sample = GameScores(created=datetime.now(), username=CustomUser.objects.get(username='testuser1'), score=50, operation='+', gamelength='30', maxnum='20', game='MATH FACTS')
        sample.save()
        self.assertTrue(sample)
        self.assertEqual(sample.username, CustomUser.objects.get(username='testuser1'))
        self.assertEqual(sample.score, 50)
        self.assertEqual(sample.operation, '+')
        self.assertEqual(sample.gamelength, '30')
        self.assertEqual(sample.maxnum, '20')
        self.assertEqual(sample.game, "MATH FACTS")

    def test_record_score_function(self):
        sample = GameScores(created=datetime.now(), username=CustomUser.objects.get(username='testuser1'), score=50, operation='+', gamelength='30', maxnum='20', game='MATH FACTS')
        sample.save()
        self.assertTrue(str(GameScores.objects.get(id=1)), 'testuser1')
        data={'username': CustomUser.objects.get(username='testuser1'), 'game': 'MATH', 'votes': 5, 'comment': 'This is a test comment.', 'created': datetime.now(), 'updated': datetime.now()}
        #request = self.client.post('/record-score/', GameScores.objects.get(id=1))
        
