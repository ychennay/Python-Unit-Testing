from unittest import TestCase

from db import db
from flask_app import app

'''
BaseTest

This class is the parent class of each non-unit test.
This allows for instantiation of the database dynamically,
ensuring that a fresh new instance of the database is created
each time.
'''


class BaseTest(TestCase):
    def setUp(self):
        # Make sure that database exists
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'

        with app.app_context():
            db.init_app(app)
            db.create_all()

        self.app = app.test_client()
        self.app_context = app.app_context

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()
