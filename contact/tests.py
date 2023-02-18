from django.test import TestCase

from htmlvalidator.client import ValidatingClient
from http import HTTPStatus

from .forms import ContactForm
from .models import Contact
from users.models import CustomUser


class ContactsTest(TestCase):
    """
    Templates, views, and urls should match up
    User should be able to fill out and submit contact form
    POST request should be valid
    """
    def setUp(self):
        super(ContactsTest, self).setUp()
        self.client = ValidatingClient()
        testuser1 = CustomUser.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        testuser1.save()
        login = self.client.force_login(testuser1)

    def test_contact_model(self):
        sample = Contact(email='emailtest@email.com', subject='Test Subject', message='This is a test')
        sample.save()
        self.assertTrue(sample)
        self.assertEqual(str(sample), "emailtest@email.com")
        self.assertEqual(sample, Contact.objects.get(email='emailtest@email.com'))
        self.assertEqual(sample.email, 'emailtest@email.com')
        self.assertEqual(sample.subject, 'Test Subject')
        self.assertEqual(sample.message, 'This is a test')

    def test_uses_contact_templates(self):
        response = self.client.get('/contact/')
        self.assertIsInstance(response.context[-1]['form'], ContactForm)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
        self.assertTemplateUsed(response, '_base.html')

    def test_user_can_submit_contact_form(self):
        data={'email': 'test@email.net', 'subject': 'Test Subject', 'message': 'This is a test message.'}
        response = self.client.post('/contact/', data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        form = ContactForm(data=data)
        self.assertTrue(form.data)

    def test_contact_form_is_valid(self):
        data={'email': 'test@email.net', 'subject': 'Test Subject', 'message': 'This is a test message.'}
        response = self.client.post('/contact/', data)
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())

    def test_contact_form_field_labels(self):
        data={'email': 'test@email.net', 'subject': 'Test Subject', 'message': 'This is a test message.'}
        response = self.client.post('/contact/', data)
        form = ContactForm(data=data)
        self.assertTrue(form.fields['email'])
        self.assertTrue(form.fields['subject'])
        self.assertTrue(form.fields['message'])

    def test_subject_and_message_max_length(self):
        contact = Contact(email="test@email.com", subject="Test Subject", message="This is a test message.")
        subject_max_length = contact._meta.get_field('subject').max_length
        self.assertEqual(subject_max_length, 100)
        message_max_length = contact._meta.get_field('message').max_length
        self.assertEqual(message_max_length, 1000)
