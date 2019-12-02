# TestCase is the base object that we will inherit
from django.test import TestCase
# substatiating it from the item form this means that we need to just import our item form
from .models import Item

# creating tests -adding a new class called TestDjango and this will inherit from TestCase and what we need to do is define a method on this class and what we want to say is test_is_this_thing_on and this will just run a little red green refactor type test

# no longer using 'class TestDjango(TestCase):'
# changng test item as per below


class TestItemModel(TestCase):

    # this test passed when 'python3 manage.py test was run' and database destroyed, so as not to dirty future tests
    # tests must begin with 'test underscore (test_), otherwise they won't run
    # no longer using 'def test_is_this_thing_on(self):'

    # testing can create item with just a name
    def test_done_defaults_to_False(self):
        item = Item(name="Create a test")
        item.save()
        self.assertEqual(item.name, "Create a test")
        # changing argument to False and getting rid of Equal, running just 1 check
        self.assertFalse(item.done)
        # self.assertEqual(item.done, False)

    def test_can_create_an_item_with_a_name_and_status(self):
        # running 2 arguments, to test when done=True
        item = Item(name="Create a test", done=True)
        item.save()
        self.assertEqual(item.name, "Create a test")
        self.assertTrue(item.done)
        # self.assertEqual(item.done,True)
