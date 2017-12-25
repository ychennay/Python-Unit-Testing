from unittest import TestCase
from unittest.mock import patch

import cli_app
from blog import Blog
from post import Post


class AppTest(TestCase):
    def setUp(self):
        b = Blog("Test Blog", "Test Author")
        b.create_post("Test Post", "Test Content")
        cli_app.blogs = {"Test": b}

    def test_print_blogs_function(self):

        with patch("builtins.print") as mocked_print:
            cli_app.print_blogs()
            mocked_print.assert_called_with("- Test Blog by Test Author (1 post)")

    def test_menu_function_calls_print(self):
        with patch("app.print_blogs") as mocked_print_blogs:
            with patch("builtins.input", return_value='q'):
                cli_app.menu()
                mocked_print_blogs.assert_called()

    def test_input_called_with_menu_prompt(self):
        with patch("builtins.input", return_value='q'):
            with patch("builtins.print") as mocked_print:
                cli_app.menu()
                mocked_print.assert_called_with("- {} by {} ({} post{})".format(
                    cli_app.blogs["Test"].title, cli_app.blogs["Test"].author, len(cli_app.blogs["Test"].posts),
                    's' if len(cli_app.blogs["Test"].posts) != 1 else ''))

    def test_ask_create_blog(self):
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ("Test Title", "Test Author")
            cli_app.ask_create_blog()
            self.assertIsNotNone(cli_app.blogs.get("Test Title"))

    def test_ask_create_post(self):
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ("Test", "Test Title", "Test Content")
            cli_app.ask_create_post()

            self.assertEqual(len(cli_app.blogs["Test"].posts), 2)
            self.assertEqual(cli_app.blogs["Test"].posts[0].title, "Test Post")
            self.assertEqual(cli_app.blogs["Test"].posts[1].title, "Test Title")

    def test_ask_read_blog(self):
        b = cli_app.blogs["Test"]
        with patch("builtins.input", return_value='Test'):
            with patch("app.print_posts") as mocked_print_posts:
                cli_app.ask_read_blog()
                mocked_print_posts.assert_called_with(b)

    def test_print_posts(self):
        b = cli_app.blogs["Test"]
        with patch("app.print_post") as mocked_print_post:
            cli_app.print_posts(b)
            mocked_print_post.assert_called_with(b.posts[0])

    def test_print_post(self):
        post = Post("Post Title", "Post Content")
        expected = cli_app.POST_TEMPLATE.format("Post Title", "Post Content")

        with patch("builtins.print") as mocked_print:
            cli_app.print_post(post)
            mocked_print.assert_called_with(expected)
