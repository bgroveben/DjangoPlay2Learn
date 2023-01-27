from django.test import TestCase
from http import HTTPStatus
from .forms import ContactForm
from .models import Contact

# Functional test for submitting contact form?
class ContactsTest(TestCase):
    """
    Templates, views, and urls should match up
    User should be able to fill out and submit contact form
    POST request should be valid
    """

    def test_uses_contact_templates(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
        self.assertTemplateUsed(response, '_base.html')

    def test_user_can_submit_contact_form(self):
        # Fill out contact form
        data={'email': 'test@email.net', 'subject': 'Test Subject', 'message': 'This is a test message.'}
        response = self.client.post('/contact/', data)
        # Make sure the form data is posted
        self.assertEqual(response.status_code, HTTPStatus.OK)
        # 2. Use posted form data to populate form
        form = ContactForm(data=data)
        # 3. Make sure that the form exists
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
        #data={'email': 'test@email.net', 'subject': 'Test Subject', 'message': 'This is a test message.'}
        #response = self.client.post('/contact/', data)
        #form = ContactForm(data=data)
        contact = Contact(email="test@email.com", subject="Test Subject", message="This is a test message.")
        subject_max_length = contact._meta.get_field('subject').max_length
        self.assertEqual(subject_max_length, 100)
        message_max_length = contact._meta.get_field('message').max_length
        self.assertEqual(message_max_length, 1000)
