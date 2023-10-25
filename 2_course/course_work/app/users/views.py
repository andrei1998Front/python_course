from flask import Blueprint, render_template, current_app
from utils import get_posts_all, get_posts_by_user

users_blueprint = Blueprint('users_blueprint', __name__, template_folder='templates')


@users_blueprint.route('/users/<poster_name>')
def user_page(poster_name):
    posts = get_posts_all(current_app.config.get('POSTS_PATH'), current_app.config.get('BOOKMARKS_PATH'))
    posts_by_user = get_posts_by_user(poster_name, posts)

    return render_template('user-feed.html', posts=posts_by_user, poster_name=poster_name)
