import json
from json import JSONDecodeError

from werkzeug.exceptions import NotFound


class FileManager:
    def __init__(self, path: str):
        self.path: str = path

    def load_data(self):
        try:
            with open(self.path, 'r') as file:
                return json.load(file)
        except (JSONDecodeError, FileNotFoundError):
            raise


class PostManager(FileManager):
    def get_posts_all(self):
        return self.load_data()

    def get_posts_by_user(self, user_name: str):
        posts = self.load_data()

        user_posts = []

        for post in posts:
            if post['poster_name'] == user_name:
                user_posts.append(post)

        return user_posts

    def search_for_posts(self, query: str):

        posts = self.load_data()

        query_posts = []

        for post in posts:
            if query.lower() in post['content'].lower():
                query_posts.append(post)

        return query_posts

    def get_post_by_pk(self, pk: int):
        posts = self.load_data()

        for post in posts:
            if post['pk'] == pk:
                return post

        raise NotFound


class CommentManager(FileManager):
    def get_comments_by_post_id(self, post_id: int):
        comments = self.load_data()

        post_comments = []

        for comment in comments:
            if comment['post_id'] == post_id:
                post_comments.append(comment)

        return post_comments


if __name__ == '__main__':
    comment_manager = CommentManager('data/comments.json')
    print(comment_manager.get_comments_by_post_id(1))
