
# creating class. In order to test our views, what we need to do is we need to ensure that we were going to the correct location i.e. the correct URL and the way to do that is to create test_views using Django framework.
from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Item

# creating class which will inherit from TestCase


class TestViews(TestCase):

    def test_get_home_page(self):
        # this is a built-in helper that will basically fake a request to the URL that we pass in as an argument here which is just forward slash and then what we can do is store the output of that in page
        page = self.client.get("/")
        # self.assertEqual(page.status_code, 200) and will check the status code property of the page object and test that it is 200
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "todo_list.html")

    def test_get_add_item_page(self):
        page = self.client.get("/add")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")

    def test_get_edit_item_page(self):
        item = Item(name="Create a Test")
        item.save()

        page = self.client.get("/edit/{0}".format(item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")

    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get("/edit/1")
        self.assertEqual(page.status_code, 404)

    def test_post_create_an_item(self):
        response = self.client.post("/add", {"name": "Create a Test"})
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, False)

    def test_post_edit_an_item(self):
        item = Item(name="Create a Test")
        item.save()
        id = item.id

        response = self.client.post(
            "/edit/{0}".format(id), {"name": "A different name"})
        item = get_object_or_404(Item, pk=id)

        self.assertEqual("A different name", item.name)

    def test_toggle_status(self):
        item = Item(name="Create a Test")
        item.save()
        id = item.id

        response = self.client.post("/toggle/{0}".format(id))

        item = get_object_or_404(Item, pk=id)
        self.assertEqual(item.done, True)
