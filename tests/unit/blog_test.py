from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):

    def test_create_blog(self):
        b = Blog("Test Title", "Test Author")

        self.assertEqual("Test Title", b.title)
        self.assertEqual("Test Author", b.author)
        self.assertListEqual(b.posts, [])

    def test_repr_method(self):
        b = Blog("Test Title", "Test Author")
        self.assertEqual(b.__repr__(), "Test Title by Test Author (0 posts)")

    def test_random_post_empty_method(self):
        pass

    def test_json(self):
        b = Blog("Test Title", "Test Author")

        expected = {
            "title": b.title,
            "author": b.author,
            "posts": []
        }

        self.assertDictEqual(b.json(),expected)