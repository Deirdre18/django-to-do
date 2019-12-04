from django.apps import apps
from django.test import TestCase
from .apps import TodoConfig


class TestTodoConfig(TestCase):
    # creating method
    def test_app(self):
        # testing can get app configuration from Django
        self.assertEqual("todo", TodoConfig.name)
        self.assertEqual("todo", apps.get_app_config("todo").name)
