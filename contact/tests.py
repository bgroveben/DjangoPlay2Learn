from django.test import TestCase
from http import HTTPStatus
from .forms import ContactForm

# Functional test for submitting contact form?
class ContactsTest(TestCase):
    """
    Templates, views, and urls should match up
    User should be able to fill out and submit contact form
    POST request should be valid
    """

    def test_uses_contact_templates(self):
        response = self.client.get('/contact/')
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
