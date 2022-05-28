import logging

from flask import Blueprint, render_template, request

from config import COMMENT_PATH, POST_PATH
from utils import CommentManager, PostManager


logger = logging.getLogger('basic')

html_bp = Blueprint('html_bp', __name__, template_folder='templates')

post_manager = PostManager(POST_PATH)
comment_manager = CommentManager(COMMENT_PATH)


@html_bp.route('/', methods=['GET'])
def feed():
    logger.info('Запрос всех постов')
    posts = post_manager.get_posts_all()

    return render_template('index.html', posts=posts)


@html_bp.route('/posts/<int:post_id>', methods=['GET'])
def post(post_id: int):
    logger.info(f'Запрос одного поста по post_id={post_id}')
    post_data = post_manager.get_post_by_pk(post_id)
    comments = comment_manager.get_comments_by_post_id(post_id)

    return render_template('post.html', post=post_data, comments=comments)


@html_bp.route('/search/', methods=['GET'])
def search():
    query = request.args.get('s', None)
    posts = post_manager.search_for_posts(query)[:10]

    return render_template('search.html', posts=posts)


@html_bp.route('/users/<string:username>', methods=['GET'])
def user_feed(username: str):
    posts = post_manager.get_posts_by_user(username)

    return render_template('user-feed.html', posts=posts)


@html_bp.app_errorhandler(404)
def not_found_errorhandler(error):
    return render_template('errors/404.html')


@html_bp.errorhandler(500)
def internal_errorhandler(error):
    return render_template('errors/500.html')


