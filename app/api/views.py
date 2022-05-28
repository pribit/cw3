import logging

from flask import Blueprint, jsonify

from config import COMMENT_PATH, POST_PATH
from utils import CommentManager, PostManager


logger = logging.getLogger('basic')

api_bp = Blueprint('api_bp', __name__, url_prefix='/api')

post_manager = PostManager(POST_PATH)
comment_manager = CommentManager(COMMENT_PATH)


@api_bp.route('/posts', methods=['GET'])
def get_posts_all():
    logger.info('Запрошены все посты по АПИ')
    posts = post_manager.get_posts_all()

    return jsonify(posts)


@api_bp.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id: int):
    logger.info(f'Запрос одного поста по АПИ post_id={post_id}')
    post = post_manager.get_post_by_pk(post_id)

    return jsonify(post)
