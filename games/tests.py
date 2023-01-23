from django.test import TestCase

class TemplatesTest(TestCase):
    # Make sure templates, views, and urls match up
    def test_uses_home_templates(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, '_base.html')
        # self.assertTemplateUsed(response, '_base_vue.html') => fail

    def test_uses_games_templates(self):
        response = self.client.get('/games/')
        self.assertTemplateUsed(response, 'games/games.html')
        self.assertTemplateUsed(response, '_base.html')
        self.assertTemplateUsed(response, '_base_vue.html')

    def test_uses_game_scores_templates(self):
        response = self.client.get('/game-scores/')
        self.assertTemplateUsed(response, 'games/game-scores.html')
        self.assertTemplateUsed(response, '_base.html')
        #self.assertTemplateUsed(response, '_base_vue.html') => fail

    def test_uses_myscores_templates(self):
        response = self.client.get('/myscores/')
        self.assertTemplateUsed(response, 'games/myscores.html')
        self.assertTemplateUsed(response, '_base.html')
        #self.assertTemplateUsed(response, '_base_vue.html') => fail
