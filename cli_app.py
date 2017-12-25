from blog import Blog

MENU_PROMPT = "Enter 'c' to create a new blog, 'p' to create a new post, " \
              "'l' to list available blogs, 'r' to read a blog, 'q' to quit"

POST_TEMPLATE = '''
    
    --- {} ---
    {}
    '''

blogs = dict()  # (blog_name, blog_object)


def menu():
    print_blogs()
    selection = input(MENU_PROMPT)

    while selection != 'q':

        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()

        selection = input(MENU_PROMPT)


def ask_create_post():
    blog_title = input("Please enter your blog title: ")
    post_title = input("Please provide a title for the post: ")
    post_content = input("Please enter in the content of your post (copy/paste it): ")

    blogs[blog_title].create_post(post_title, post_content)


def ask_read_blog():
    blog_title = input("Please provide the title of the blog you want to read: ")
    print_posts(blogs[blog_title])


def ask_create_blog():
    blog_title = input("Please provide a title for the blog: ")
    blog_author = input("Please provide an author for the blog: ")
    blogs[blog_title] = Blog(blog_title, blog_author)


def print_blogs():
    for blog_name, blog_object in blogs.items():
        print("- {}".format(blog_object))


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))
