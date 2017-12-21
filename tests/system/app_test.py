from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post


class AppTest(TestCase):
    def test_print_blogs_function(self):
        b = Blog("Test Blog", "Test Author")
        app.blogs = {"Test": b}

        with patch("builtins.print") as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with("- Test Blog by Test Author (0 posts)")

    def test_menu_function_calls_print(self):
        with patch("app.print_blogs") as mocked_print_blogs:
            with patch("builtins.input"):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_input_called_with_menu_prompt(self):
        with patch("builtins.input") as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_ask_create_blog(self):
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ("Test Title", "Test Author")
            app.ask_create_blog()
            self.assertIsNotNone(app.blogs.get("Test Title"))

    def test_ask_read_blog(self):
        b = Blog("Test Blog", "Test Author")
        app.blogs = {"Test": b}

        with patch("builtins.input", return_value='Test Title'):
            with patch("app.print_posts") as mocked_print_posts:
                mocked_print_posts.assert_called_with(b)

    def test_print_posts(self):
        b = Blog("Test Blog", "Test Author")
        b.create_post("Test Post", "Test Content")
        app.blogs = {"Test": b}

        with patch("app.print_post") as mocked_print_post:
            app.print_posts(b)
            mocked_print_post.assert_called_with(b.posts[0])

    def test_print_post(self):
        post = Post("Post Title", "Post Content")
        expected = app.POST_TEMPLATE.format("Post Title", "Post Content")

        with patch("builtins.print") as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected)
