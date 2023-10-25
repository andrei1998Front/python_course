from flask import Blueprint, render_template, current_app
from utils import *

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    bookmarks = get_bookmarks_all(current_app.config.get('BOOKMARKS_PATH'))
    posts = get_posts_all(current_app.config.get('POSTS_PATH'), current_app.config.get('BOOKMARKS_PATH'))
    return render_template('index.html', posts=posts, bookmarks=bookmarks)
