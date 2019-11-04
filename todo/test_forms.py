# TestCase is the base object that we will inherit
from django.test import TestCase
# substatiating it from the item form this means that we need to just import our item form
from .forms import ItemForm

# creating tests -adding a new class called TestDjango and this will inherit from TestCase and what we need to do is define a method on this class and what we want to say is test_is_this_thing_on and this will just run a little red green refactor type test

# no longer using 'class TestDjango(TestCase):'
# changng test item as per below


class TestToDoItemForm(TestCase):

    # this test passed when 'python3 manage.py test was run' and database destroyed, so as not to dirty future tests
    # tests must begin with 'test underscore (test_), otherwise they won't run
    # no longer using 'def test_is_this_thing_on(self):'

    # testing can create item with just a name
    def test_can_create_item_with_just_a_name(self):

        # can instantiate this object using a dictionary so we will open our curly braces for a dictionary and the key is going to be name and then the value is going to be a string that we wish to give it so we'll give this a key of name we'll give it a value of create tests
        # no longer using 'form = ItemForm({'name': 'Create Tests'})'
        # this is a boolean of not true
        # no longer using 'self.assertTrue(form.is_valid())'

        # change this to assert false our test would fail because the value returned isn't false, the value we get returned is true so we can see that we have one failure there if we run that test and the assertion error is true it's not false
        # no longer using 'self.assertFalse(form.is_valid())''
        # changing value back to True
        # no longer using 'self.assertTrue(form.is_valid())''
        # no longer using 'self.assertEqual(1, 1)'

        # another method now that will test to ensure that the form validate the item cannot be created if we don't create a name and we'll assert that we get the correct message

        def test_correct_message_for_missing_name(self):
            form = ItemForm({'form': ''})
            self.assertFalse(form.is_valid())
        # there is an error in the name and we want to assert that the value that the error gives back is a string that says this field is required with a full stop at the end. Full stop at the end because otherwise our test will fail, as it looks for an exact match and this field is required as a standard piece of text that Django will get back when form validation fails
            self.assertEqual(form.errors['name'], [u'This field is required.'])
