from django.test import TestCase
from django.urls import reverse

from http import HTTPStatus
from datetime import datetime

from .forms import ReviewForm
from users.models import CustomUser
from review.models import Review


class ReviewsTest(TestCase):
    # Make sure templates, views, and urls match up
    # Only logged in users can submit a review

    def setUp(self):
        testuser1 = CustomUser.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        testuser1.save()
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')

    def test_uses_home_templates(self):
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
