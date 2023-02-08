from django.test import TestCase
#from django.db import models
#from django import forms
#from datetime import datetime
#from django.contrib.auth.forms import UserChangeForm
#from django.contrib.auth import get_user_model
from django.urls import reverse
from http import HTTPStatus

from users.models import CustomUser
#from users.forms import CustomUserChangeForm


class CustomUserModelTest(TestCase):

    def setUp(self):
        # Create test user
        testuser1 = CustomUser.objects.create_user(
                            username='testuser1',
                            password='1X<ISRUkw+tuK',
                            email='test@email.com',
                            first_name='test',
                            last_name='user',
                            dob='1980-01-01'
                            #dob=str(models.DateField(1980,1,1))
                            )
        testuser1.save()
        login = self.client.login(username=testuser1,
                                password='1X<ISRUkw+tuK'
                                )


    def test_custom_user_field_labels(self):
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

    def test_sample_custom_user_model(self):
        sample = CustomUser.objects.get(id=1)
        self.assertTrue(sample)
        self.assertEqual(sample.username, 'testuser1')
        self.assertIsInstance(sample, CustomUser)


    def test_user_can_update_their_account_form(self):
        data={'email': 'test@email.com', 'username': 'testuser1', 'first_name': 'test', 'last_name': 'user', 'dob': '1980'}
        response = self.client.post('/users/my-account/', data)
        response = self.client.post(reverse('users:my_account'), data)
        # Make sure the form data is posted
        self.assertTrue(response)
        self.assertEqual(response.status_code, HTTPStatus.OK)

