# TestCase is the base object that we will inherit
from django.test import TestCase

# creating tests -adding a new class called TestDjango and this will inherit from TestCase and what we need to do is define a method on this class and what we want to say is test_is_this_thing_on and this will just run a little red green refactor type test


class TestDjango(TestCase):

    # this test passed when 'python3 manage.py test was run' and database destroyed, so as not to dirty future tests
    # tests must begin with 'test underscore (test_), otherwise they won't run
    def test_is_this_thing_on(self):
        self.assertEqual(1, 1)
