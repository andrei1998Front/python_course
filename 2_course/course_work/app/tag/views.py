from flask import Blueprint, render_template, current_app
from utils import get_posts_by_tag, get_posts_all

tag_blueprint = Blueprint('tag_blueprint', __name__, template_folder='templates')


@tag_blueprint.route('/tag/<tag>')
def tag_page(tag):
    posts = get_posts_all(current_app.config.get('POSTS_PATH'), current_app.config.get('BOOKMARKS_PATH'))
    posts_by_tag = get_posts_by_tag(tag, posts)

    return render_template('tag.html', posts=posts_by_tag, tag=tag)