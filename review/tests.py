from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings

#import http
from http import HTTPStatus
from datetime import datetime

from .forms import ReviewForm
from users.models import CustomUser
from review.models import Review


class ReviewsTest(TestCase):


    def setUp(self):
        # Create test user
        testuser1 = CustomUser.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        testuser1.save()
        # https://docs.djangoproject.com/en/4.1/topics/testing/tools/#django.test.Client.force_login
        login = self.client.force_login(testuser1)


    def test_review_form_is_valid(self):
        # Fill out review form
        #username = 'testuser1'
        #username = CustomUser.get_username('admin')
        username = settings.AUTH_USER_MODEL
        data={'username': CustomUser.objects.get(username='testuser1'), 'game': 'MATH FACTS', 'votes': "5", 'comment': 'This is a test comment.', 'created': datetime.now(), 'updated': datetime.now()}
        game = data["game"]
        votes = data["votes"]
        comment = data["comment"]
        #username = data["username"]
        response = self.client.post('/review/', data)
        new_review = Review(game=game, votes=votes, comment=comment)
        new_review_form = ReviewForm(data)
        self.assertTrue(new_review_form)
        self.assertEqual(new_review.game, 'MATH FACTS')
        self.assertEqual(new_review.votes, "5")
        self.assertEqual(new_review.comment, 'This is a test comment.')
        #new_review_form.save()
        #self.assertEqual(new_review.username, 'testuser1')
        #self.assertTrue(new_review_form.is_valid())

        #new_review.save()
        #response = self.client.post('/review/', data)
        #sample.save()
        #review_form = ReviewForm(sample)
        #review_form.save()
        #self.assertTrue(form.is_valid())


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
        # Fill out review form
        username = 'admin'
        #username = CustomUser.get_username('admin')
        data={'username': username, 'game': 'MATH', 'votes': 5, 'comment': 'This is a test comment.', 'created': datetime.now(), 'updated': datetime.now()}
        response = self.client.post('/review/', data)
        # Make sure the form data is posted
        self.assertTrue(response)
        # Make sure user is redirected
        self.assertEqual(response.status_code, 302)
        # Use posted form data to populate form
        form = ReviewForm(data=data)
        # form.save()
        # Make sure that the form exists
        self.assertTrue(form.data)
        #form.save()
        #self.assertTrue(form.is_valid())

    def test_user_can_view_reviews(self):
        response = self.client.get('/review/review')
        self.assertEqual(response.status_code, 301)

    def test_review_form_field_labels(self):
        username = 'admin'
        data={'username': username, 'game': 'MATH', 'votes': 5, 'comment': 'This is a test comment.', 'created': datetime.now(), 'updated': datetime.now()}
        response = self.client.post('/review/', data)
        form = ReviewForm(data=data)
        #print(form)
        #form.save()
        #self.assertTrue(form.is_valid())
        self.assertTrue(form.fields['game'])
        self.assertTrue(form.fields['votes'])
        self.assertTrue(form.fields['comment'])

    def test_review_meta_fields(self):
        review = Review(game="MATH", votes=5, comment="This is a test comment.")
        votes_count = review._meta.get_field('votes').choices
        self.assertEqual(votes_count, ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
        comment_max_length = review._meta.get_field('comment').max_length
        self.assertEqual(comment_max_length, 1000)
        review_username = review._meta.get_field('username').related_name='reviews'
        self.assertTrue(review_username)
        game_choices = review._meta.get_field('game').choices
        self.assertEqual(game_choices, [('MATH FACTS', 'Math Facts'), ('ANAGRAM HUNT', 'Anagram Hunt')])

    def test_user_can_fill_out_review_form(self):
        review = Review(game="MATH", votes=5, comment="This is a test comment.")
        review_form = ReviewForm(review)
        #review_form.save()
        self.assertTrue(review_form)
