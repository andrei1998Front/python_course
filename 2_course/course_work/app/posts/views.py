from flask import Blueprint, render_template, current_app
from utils import *

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')

@posts_blueprint.route('/posts/<int:pk>')
def main_page(pk):
    posts = get_posts_all(current_app.config.get('POSTS_PATH'), current_app.config.get('BOOKMARKS_PATH'))
    post = get_post_by_pk(pk, posts)
    post_comments = get_comments_by_post_id(pk, current_app.config.get('COMMENTS_PATH'), posts)
    return render_template('post.html', post=post, post_comments=post_comments)
