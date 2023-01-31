from django.test import TestCase
from django.urls import reverse

from http import HTTPStatus
from datetime import datetime

from .forms import ReviewForm
from users.models import CustomUser
from review.models import Review


class ReviewsTest(TestCase):
    """
    Make sure templates, views, and urls match up
    Only logged in users can submit a review
    View uses @login_required decorator
    """

    def setUp(self):
        # Create test user
        testuser1 = CustomUser.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        testuser1.save()
        login = self.client.login(username=testuser1, password='1X<ISRUkw+tuK')

    def test_review_model(self):
        sample = Review(username=CustomUser.objects.get(username='testuser1'), game='MATH FACTS', votes=3, comment="This is a test comment", created=datetime.now, updated=datetime.now)
        sample.save()
        #print(sample)
        self.assertTrue(sample)
        self.assertEqual(str(sample), "MATH FACTS")
        self.assertEqual(sample.username, CustomUser.objects.get(username='testuser1'))
        self.assertEqual(sample.game, "MATH FACTS")
        self.assertEqual(sample.votes, 3)
        self.assertEqual(sample.comment, "This is a test comment")
        self.assertTrue(sample.created)
        self.assertTrue(sample.updated)

    def test_uses_review_template(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, '_base.html')

    def test_user_can_submit_review_form(self):
        # Fill out contact form
        username = 'admin'
        #username = CustomUser.get_username('admin')
        data={'username': username, 'game': 'MATH', 'votes': 5, 'comment': 'This is a test comment.', 'created': datetime.now(), 'updated': datetime.now()}
        response = self.client.post('/review/', data)
        # Make sure the form data is posted
        self.assertEqual(response.status_code, HTTPStatus.OK)
        # 2. Use posted form data to populate form
        form = ReviewForm(data=data)
        # 3. Make sure that the form exists
        self.assertTrue(form.data)

    def test_view_url_is_accessible(self):
        # Fill out contact form
        username = 'TestUser'
        #username = CustomUser.get_username('admin')
        data={'username': username, 'game': 'MATH', 'votes': 5, 'comment': 'This is a test comment.', 'created': datetime.now(), 'updated': datetime.now()}
        response = self.client.post('/review/', data)
        #response = self.client.get('/review/', data)  -> also works
        #review = self.client.get('/review/review')  301 != 200 -> redirect?
        self.assertEqual(response.status_code, 200)
