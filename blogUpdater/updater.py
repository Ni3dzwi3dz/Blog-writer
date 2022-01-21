import config
import os
from httplib2 import Http
from oauth2client.file import Storage
from oauth2client import tools
from oauth2client.client import flow_from_clientsecrets, OAuth2Credentials
from googleapiclient.discovery import build


class BlogUpdater:

    def __init__(self) -> None:
        self.http = Http()
        self.credentials = self.authorize()
        self.service = self.build_service()

    def authorize(self) -> OAuth2Credentials:

        credential_dir = os.path.join(os.path.dirname(__file__), 'cached_oauth_credentials')

        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir, 'googleapis.json')

        store = Storage(credential_path)
        credentials = store.get()

        if not credentials:
            flow = flow_from_clientsecrets(config.CREDENTIALS, scope=config.SCOPES)
            flow.user_agent = config.USER_AGENT
            credentials = tools.run_flow(
                flow,
                store,
                tools.argparser.parse_args(args=['--noauth_local_webserver']))
            store.put(credentials)
        else:
            credentials.refresh(self.http)

        return credentials

    def build_service(self):

        if not self.credentials:
            self.authorize()

        service = build('blogger', 'v3', credentials=self.credentials)
        
        return service

    def get_blog_id(self) -> str:
        blogs = self.service.blogs()
        response = blogs.get(blogId=config.BLOG_ID, maxPosts=3, view='ADMIN').execute()
        return str(response)

    def get_published(self) -> list:

        posts = self.service.posts()

        published = posts.list(blogId=config.BLOG_ID).execute()

        return [item for item in published['items']]

    def validate_posts(self, list_of_posts: list) -> list:

        already_published = [item['title'] for item in self.get_published()]

        return [post for post in list_of_posts if post['title'] not in already_published]

    def post_to_blog(self, list_of_posts: list) -> None:

        posts = self.service.posts()

        # First, i want to doublecheck if i am not posting something that is already on the blog
        posts_to_publish = self.validate_posts(list_of_posts)

        # Google limits free actions to 10 requests
        # therefore, i can only take first ten posts

        if len(posts_to_publish) > 10:
            posts_to_publish = posts_to_publish[:10]

        for post in posts_to_publish:
            response = posts.insert(blogId=config.BLOG_ID, body=post).execute()
            print(response['url'])


if __name__ == '__main__':
    updater = BlogUpdater()
    updater.get_blog_id()
