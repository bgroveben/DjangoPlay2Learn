from django.test import TestCase


class TemplatesTest(TestCase):
    # Make sure templates, views, and urls match up
    def test_uses_reviews_template(self):
        response = self.client.get('/users/my-account/')
        self.assertTemplateUsed(response, 'account/my-account.html')
        self.assertTemplateUsed(response, '_base.html')

    def test_uses_reviews_template(self):
        response = self.client.get('/users/reviews/')
        self.assertTemplateUsed(response, 'users/reviews.html')
        self.assertTemplateUsed(response, '_base.html')

    def test_uses_reviewspage_template(self):
        response = self.client.get('/users/reviewspage/')
        self.assertTemplateUsed(response, 'users/reviewspage.html')
        self.assertTemplateUsed(response, '_base.html')
