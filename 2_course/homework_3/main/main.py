import logging

from flask import render_template, request, Blueprint
from functions import get_posts_from_json

logging.basicConfig(filename="basic.log", level=logging.INFO)

main_blueprint = Blueprint('main_blueprint', __name__, url_prefix="/", template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search')
def search_page():
    search_string = request.args.get('s').lower()

    found_posts = [post for post in get_posts_from_json() if search_string in post['content'].lower()]
    logging.info(f"Поиск по значению {search_string}")

    return render_template('post_list.html', found_posts=found_posts, search_string=search_string)
