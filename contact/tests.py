from django.test import TestCase

class TemplatesTest(TestCase):
    # Make sure templates, views, and urls match up
    def test_uses_contact_templates(self):
        response = self.client.get('/contact/')
        self.assertTemplateUsed(response, 'contact/contact.html')
        self.assertTemplateUsed(response, '_base.html')
