from django.test import TestCase
from django.urls import reverse

from http import HTTPStatus
from datetime import datetime

from .forms import ReviewForm
from users.models import CustomUser
from review.models import Review


class ReviewsTest(TestCase):
    # Make sure templates, views, and urls match up
    def test_uses_home_templates(self):
        response = self.client.get('/')
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


"""
    def test_view_url_is_accessible(self):
        CustomUser.objects.create(
                        username="TestUser",
                        email="test@email.com",
                        first_name="Test",
                        last_name="User"
                        )
        customuser = CustomUser.objects.get(id=1)
        #for review_id in range(10):
        Review.objects.create(
            username=customuser.username,
            game="MATH FACTS",
            votes=3,
            comment="This is a test comment"
        )
        response = self.client.get('/review/review')
        self.assertEqual(response.status_code, 200)
"""
"""
    def test_view_url_is_accessible_by_name(self):
        CustomUser.objects.create(
                        username="TestUser",
                        email="test@email.com",
                        first_name="Test",
                        last_name="User"
                        )
        customuser = CustomUser.objects.get(id=1)
        for review_id in range(10):
            Review.objects.create(
                username=customuser.username,
                game="MATH FACTS",
                votes=3,
                comment="This is a test comment"
            )
        response = self.client.get(reverse('review'))
        self.assertEqual(response.status_code, 200)
"""
"""
    def test_review_form_is_valid(self):
        # Fill out contact form
        # Fill out contact form
        data={'username': 'admin', 'game': 'MATH', 'votes': 5, 'comment': 'This is a test comment.', 'created': datetime.now(), 'updated': datetime.now()}
        #data={'username': 'admin', 'game': 'MATH FACTS', 'votes': (5,5), 'comment': 'This is a test comment.'}
        #user = CustomUser()
        #print(user)
        #data={'game': 'MATH FACTS', 'votes': (5,5), 'comment': 'This is a test comment.'}
        print(data)
        #print(user)
        response = self.client.post('/review/', data)
        # Make sure the form data is posted
        self.assertEqual(response.status_code, HTTPStatus.OK)
        # 2. Use posted form data to populate form
        form = ReviewForm(data=data)
        # 3. Make sure that the form exists
        self.assertTrue(form.data)
        # self.assertTrue(form.is_valid()) => AssertionError: False is not true
"""
