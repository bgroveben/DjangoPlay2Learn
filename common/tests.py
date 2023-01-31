#from django.test import TestCase -- common isn't a django app, just a directory
import unittest

from common.templatetags import common_filters
from common.utils import email


class SwapValuesFunctionTest(unittest.TestCase):

    def test_swap_addition(self):
        addition = common_filters.swap('+')
        self.assertTrue(addition)
        self.assertEqual(addition, 'Addition')

    def test_swap_subtraction(self):
        subtraction = common_filters.swap('-')
        self.assertTrue(subtraction)
        self.assertEqual(subtraction, 'Subtraction')

    def test_swap_multiplication(self):
        multiplication = common_filters.swap('x')
        self.assertTrue(multiplication)
        self.assertEqual(multiplication, 'Multiplication')

    def test_swap_division(self):
        division = common_filters.swap('/')
        self.assertTrue(division)
        self.assertEqual(division, 'Division')

    def test_numeric_inputs_are_swapped(self):
        numbers = ['5','6','7','8']
        for number in numbers:
            self.assertTrue(common_filters.swap(number))
            self.assertEqual(common_filters.swap(number), 'Anagram Hunt')


class UserCanSendEmailTest(unittest.TestCase):

    def test_user_can_submit_message(self):
        message = email.send_email('test@example.com', 'Test Subject', 'This is a test')
        self.assertTrue(message)
