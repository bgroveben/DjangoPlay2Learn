from django.test import TestCase 

from common.templatetags import common_filters
from common.utils import email
from common.utils import admin 


class AppendMoveRemoveFunctionsTest(TestCase):

    def test_append_new_field_to_a_fieldset_in_fieldsets(self):
        fieldtest = admin.append_fields(('username',), None, ('email',))
        self.assertTrue(fieldtest)
        self.assertIsInstance(fieldtest, tuple)
        self.assertEqual(fieldtest, ('username', (None, {'classes': ('wide',), 'fields': ('email',)})))

    def test_remove_fields_from_fieldset_in_fieldsets(self):
        fieldappend = admin.append_fields(('username',), 'review', ('email',))
        fieldremove = admin.remove_fields(fieldappend, 'review', ('email',))
        self.assertTrue(fieldremove)
        self.assertIsInstance(fieldremove, tuple)
        self.assertEqual(fieldremove, ('username', ('review', {'classes': ('wide',), 'fields': ()})))

    def test_moves_fields_from_from_fieldset_to_to_fieldset_in_fieldset(self):
        newfield = admin.append_fields(('username',), 'review', ('email',))
        fieldmove = admin.move_fields(newfield, 'review', 'games', ('email',))
        self.assertTrue(fieldmove)
        self.assertIsInstance(fieldmove, tuple)
        self.assertEqual(fieldmove, ('username', ('review', {'classes': ('wide',), 'fields': ()})))
        # sanity check - returns same results as remove_fieldset test above 

    def test_exception_in_move_fields_function(self):
        fieldappend = admin.append_fields(('username',), 'review', ('email',))
        fieldremove = admin.remove_fields(fieldappend, 'review', ('email',))
        self.assertTrue(fieldremove)
        with self.assertRaises(Exception):
            fieldmove = admin.move_fields(('username', (None, {'classes': ('wide',), 'fields': ('email',)})), 'review', 'games', ('email',))
                        

class SwapValuesFunctionTest(TestCase):

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


class UserCanSendEmailTest(TestCase):

    def test_user_can_submit_message(self):
        message = email.send_email('test@example.com', 'Test Subject', 'This is a test')
        self.assertTrue(message)
