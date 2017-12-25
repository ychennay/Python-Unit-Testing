import json

from tests.system.base_test import BaseTest


class TestHome(BaseTest):
    def test_home(self):
        with self.app as c:
            response = c.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.get_data()),
                             {'message': 'Hello world!'})
