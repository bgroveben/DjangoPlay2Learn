from django.test import TestCase

class TemplatesTest(TestCase):
    # Make sure templates, views, and urls match up
    def test_uses_home_templates(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, '_base.html')
        # self.assertTemplateUsed(response, '_base_vue.html') => fail
