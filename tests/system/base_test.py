from unittest import TestCase

from flask_app import app


class BaseTest(TestCase):
    def setUp(self):
        self.app = app.test_client()
