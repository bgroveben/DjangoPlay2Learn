from django.test import TestCase
from django.db import models

from datetime import datetime
from htmlvalidator.client import ValidatingClient

from users.models import CustomUser
from .models import GameScores
from .views import HomeView, GamesView, GameScoresView, MyScoresView


class TemplatesTest(TestCase):

    def setUp(self):
        super(TemplatesTest, self).setUp()
        self.client = ValidatingClient()
        testuser1 = CustomUser.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        testuser1.save()
        login = self.client.force_login(testuser1)
        
    def test_uses_home_templates(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context[-1]['view'], HomeView)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, '_base.html')

    def test_uses_games_templates(self):
        response = self.client.get('/games/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context[-1]['view'], GamesView)
        self.assertTemplateUsed(response, 'games/games.html')
        self.assertTemplateUsed(response, '_base_vue.html')

    def test_uses_game_scores_templates(self):
        response = self.client.get('/game-scores/')
        self.assertIsInstance(response.context[-1]['view'], GameScoresView)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'games/game-scores.html')
        self.assertTemplateUsed(response, '_base.html')

    def test_uses_myscores_templates(self):
        response = self.client.get('/myscores/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context[-1]['view'], MyScoresView)
        self.assertTemplateUsed(response, 'games/myscores.html')
        self.assertTemplateUsed(response, '_base.html')


class GameScoresTest(TestCase):

    def setUp(self):
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

    def test_game_scores_meta_fields(self):
        sample = GameScores(created=datetime.now(), username=CustomUser.objects.get(username='testuser1'), score=50, operation='+', gamelength='30', maxnum='20', game='MATH FACTS')
        createds = sample._meta.get_field('created')
        self.assertTrue(createds)
        self.assertIsInstance(createds, models.DateTimeField)
        usernames = sample._meta.get_field('username')
        self.assertTrue(usernames)
        self.assertIsInstance(usernames, models.TextField)
        scores = sample._meta.get_field('score')
        self.assertTrue(scores)
        self.assertIsInstance(scores, models.IntegerField)
        gamelengths = sample._meta.get_field('gamelength')
        self.assertTrue(gamelengths)
        self.assertIsInstance(gamelengths, models.TextField)
        maxnums = sample._meta.get_field('maxnum')
        self.assertTrue(maxnums)
        self.assertIsInstance(maxnums, models.TextField)
        operations = sample._meta.get_field('operation')
        self.assertTrue(operations)
        self.assertIsInstance(operations, models.TextField)
        games = sample._meta.get_field('game')
        self.assertTrue(games)
        self.assertIsInstance(games, models.TextField)

