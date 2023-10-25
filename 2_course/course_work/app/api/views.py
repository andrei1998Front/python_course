import logging

from flask import Blueprint, jsonify, current_app
from utils import get_posts_all, get_post_by_pk

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler(filename='./logs/api.log', encoding='utf-8')

logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", handlers=[file_handler], level=logging.INFO,
                    datefmt='%Y.%m.%d %I:%M:%S %p')

api_blueprint = Blueprint('api_blueprint', __name__, url_prefix='/api/')


@api_blueprint.route('/posts')
def get_posts_json():
    logging.info('Запрос /api/posts')

    posts = get_posts_all(current_app.config.get('POSTS_PATH'), current_app.config.get('BOOKMARKS_PATH'))
    return jsonify(posts)


@api_blueprint.route('/posts/<int:post_id>')
def get_post_by_pk_json(post_id):
    logging.info(f'Query to /api/posts/{post_id}')

    posts = get_posts_all(current_app.config.get('POSTS_PATH'), current_app.config.get('BOOKMARKS_PATH'))
    post = get_post_by_pk(post_id, posts)
    return jsonify(post)
