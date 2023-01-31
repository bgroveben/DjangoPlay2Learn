from django.test import TestCase

from django.urls import reverse

from users.models import CustomUser

"""
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing

This class demonstrates how to construct a test case class by deriving from TestCase.

class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)

"""

class TemplatesTest(TestCase):
    # Make sure templates, views, and urls match up

    def test_uses_reviews_template(self):
        response = self.client.get('/users/reviews/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/reviews.html')
        self.assertTemplateUsed(response, '_base.html')

    def test_uses_reviewspage_template(self):
        response = self.client.get('/users/reviewspage/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/reviewspage.html')
        self.assertTemplateUsed(response, '_base.html')


class CustomUserModelTest(TestCase):

    def setUp(self):
        # Create test user
        testuser1 = CustomUser.objects.create_user(
                            username='testuser1',
                            password='1X<ISRUkw+tuK'
                            )
        testuser1.save()
        login = self.client.login(username=testuser1,
                                password='1X<ISRUkw+tuK'
                                )

    def test_field_labels(self):
        customuser = CustomUser.objects.get(id=1)
        username_label = customuser._meta.get_field('username').verbose_name
        self.assertEqual(username_label, 'username')
        email_label = customuser._meta.get_field('email').verbose_name
        self.assertEqual(email_label, 'email address')
        first_name_label = customuser._meta.get_field('first_name').verbose_name
        self.assertEqual(first_name_label, 'first name')
        last_name_label = customuser._meta.get_field('last_name').verbose_name
        self.assertEqual(last_name_label, 'last name')
        dob_label = customuser._meta.get_field('dob').verbose_name
        self.assertEqual(dob_label, 'Date of Birth')
        avatar_label = customuser._meta.get_field('avatar').verbose_name
        self.assertEqual(avatar_label, 'Your Image')

    def test_customuser_model(self):
        sample = CustomUser.objects.get(id=1)
        #sample.save()
        self.assertTrue(sample)
        self.assertEqual(sample.username, 'testuser1')
