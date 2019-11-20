
# creating class. In order to test our views, what we need to do is we need to ensure that we were going to the correct location i.e. the correct URL and the way to do that is to create test_views using Django framework.
from django.test import TestCase

# creating class which will inherit from TestCase


class TestViews(TestCase):

    def test_get_home_page(self):
        # this is a built-in helper that will basically fake a request to the URL that we pass in as an argument here which is just forward slash and then what we can do is store the output of that in page
        page = self.client.get("/")
        # self.assertEqual(page.status_code, 200) and will check the status code property of the page object and test that it is 200
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "todo_list.html")
