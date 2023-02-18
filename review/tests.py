from django.test import TestCase
from htmlvalidator.client import ValidatingClient
from datetime import datetime
from django.http.response import HttpResponsePermanentRedirect

from .forms import ReviewForm
from users.models import CustomUser
from review.models import Review
from .views import ReviewView, MyReviewsView


class ReviewsTest(TestCase):

    def setUp(self):
        super(ReviewsTest, self).setUp()
        self.client = ValidatingClient()
        # Create test user
        testuser1 = CustomUser.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        testuser1.save()
        # https://docs.djangoproject.com/en/4.1/topics/testing/tools/#django.test.Client.force_login
        login = self.client.force_login(testuser1)

    def test_uses_review_home_template(self):
        response = self.client.get('/review/')
        self.assertIsInstance(response.context[-1]['form'], ReviewForm)
        self.assertTemplateUsed(response, 'review/home.html')
        self.assertTemplateUsed(response, '_base.html')
        self.assertEqual(response.status_code, 200)

    def test_uses_review_review_template(self):
        response = self.client.get('/review/review/')
        self.assertIsInstance(response.context[-1]['view'], ReviewView)
        self.assertTemplateUsed(response, 'review/reviews.html')
        self.assertTemplateUsed(response, '_base.html')
        self.assertEqual(response.status_code, 200)

    def test_uses_my_reviews_template(self):
        response = self.client.get('/review/myreviews/')
        self.assertIsInstance(response.context[-1]['view'], MyReviewsView)
        self.assertTemplateUsed(response, 'review/myreviews.html')
        self.assertTemplateUsed(response, '_base.html')
        self.assertEqual(response.status_code, 200)

    def test_uses_delete_review(self):
        username = 'admin'
        data={'username': username, 'game': 'MATH', 'votes': 5, 'comment': 'This is a test comment.', 'created': datetime.now(), 'updated': datetime.now()}
        response = self.client.post('/review/', data)
        removed = self.client.delete('/review/review/1/delete')
        self.assertTrue(removed)
        self.assertEqual(removed.status_code, 301)
        self.assertIsNone(removed.context)
        self.assertIsInstance(removed, HttpResponsePermanentRedirect)

    def test_uses_update_review(self):
        username = 'admin'
        data={'username': username, 'game': 'MATH', 'votes': 5, 'comment': 'This is a test comment.', 'created': datetime.now(), 'updated': datetime.now()}
        response = self.client.post('/review/', data)
        updated = self.client.post('/review/review/1/update')
        self.assertTrue(updated)
        self.assertEqual(updated.status_code, 301)
        self.assertIsNone(updated.context)
        self.assertIsInstance(updated, HttpResponsePermanentRedirect)
        
    def test_user_can_GET_myreviews_page(self):
        response = self.client.get('/review/myreviews/')
        # only registered users, aka, CustomUsers can submit reviews
        self.assertIsInstance(response.context[-1]["user"], CustomUser)
        self.assertEqual(response.context["user"].id, 1)
        self.assertContains(response, "game")
        self.assertContains(response, "user")
        self.assertEqual(response.context["user"].id, 1)
        self.assertEqual(response.status_code, 200)

    def test_user_can_fill_out_review_form(self):
        review = Review(game="MATH", votes=5, comment="This is a test comment.")
        review_form = ReviewForm(review)
        self.assertTrue(review_form)
        self.assertIsInstance(review_form, ReviewForm)

    def test_user_can_GET_review_page(self):
        response = self.client.get('/review/')
        self.assertContains(response, "game")
        self.assertContains(response, "user")
        self.assertEqual(response.status_code, 200)
        
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
        # Make sure that the form exists
        self.assertTrue(form.data)
        #self.assertTrue(form.is_valid())

    def test_review_form_field_labels(self):
        username = 'admin'
        data={'username': username, 'game': 'MATH', 'votes': 5, 'comment': 'This is a test comment.', 'created': datetime.now(), 'updated': datetime.now()}
        form = ReviewForm(data=data)
        self.assertTrue(form.fields['game'])
        self.assertTrue(form.fields['votes'])
        self.assertTrue(form.fields['comment'])

    def test_user_can_POST_review_using_form(self):
        data={'username': CustomUser.objects.get(username='testuser1').id, 'game': 'MATH FACTS', 'votes': 5, 'comment': 'This is a test comment.', 'created': datetime.now(), 'updated': datetime.now()}
        response = self.client.post('/review/', data=data)
        self.assertTrue(response)
        self.assertEqual(Review.objects.count(), 1)
        self.assertRedirects(response, '/review/review/')
        self.assertEqual(response.status_code, 302)
        game = data["game"]
        votes = data["votes"]
        comment = data["comment"]
        new_review = Review(game=game, votes=votes, comment=comment)
        new_review_form = ReviewForm(data)
        self.assertTrue(new_review_form)
        self.assertEqual(new_review.game, 'MATH FACTS')
        self.assertEqual(new_review.votes, 5)
        self.assertEqual(new_review.comment, 'This is a test comment.')
        self.assertTrue(new_review_form.is_valid())

    def test_review_model(self):
        sample = Review(username=CustomUser.objects.get(username='testuser1'), game='MATH FACTS', votes=3, comment="This is a test comment", created=datetime.now, updated=datetime.now)
        sample.save()
        self.assertTrue(sample)
        self.assertEqual(str(sample), "MATH FACTS")
        self.assertEqual(sample.username, CustomUser.objects.get(username='testuser1'))
        self.assertEqual(sample.game, "MATH FACTS")
        self.assertEqual(sample.votes, 3)
        self.assertEqual(sample.comment, "This is a test comment")
        self.assertTrue(sample.created)
        self.assertTrue(sample.updated)

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

