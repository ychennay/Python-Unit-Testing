from unittest import TestCase
from blog import Blog
from post import Post


class BlogTest(TestCase):

    def test_create_post_method(self):
        b = Blog("Test Title", "Test Author")
        b.create_post("New Post", "New Content")

        self.assertEqual(1, len(b.posts))
        self.assertIsInstance(b.posts[0], Post)
