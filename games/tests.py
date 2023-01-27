from django.test import TestCase

from django.urls import reverse_lazy

from users.models import CustomUser


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
