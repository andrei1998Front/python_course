from flask import Blueprint, render_template, redirect, current_app
from utils import *

bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__, template_folder='templates')


@bookmarks_blueprint.route('/bookmarks/')
def bookmarks_page():
    posts = get_posts_all(current_app.config.get('POSTS_PATH'), current_app.config.get('BOOKMARKS_PATH'))
    bookmarks = get_bookmarks_all(current_app.config.get('BOOKMARKS_PATH'))

    posts_by_bookmarks = get_posts_by_bookmarks(posts, bookmarks)

    return render_template('bookmarks.html', posts=posts_by_bookmarks)


@bookmarks_blueprint.route('/bookmarks/add/<int:post_id>')
def bookmarks_add(post_id):
    posts = get_posts_all(current_app.config.get('POSTS_PATH'), current_app.config.get('BOOKMARKS_PATH'))
    bookmarks = get_bookmarks_all(current_app.config.get('BOOKMARKS_PATH'))
    add_bookmark(current_app.config.get('BOOKMARKS_PATH'), post_id, bookmarks, posts)

    return redirect('/', 302)


@bookmarks_blueprint.route('/bookmarks/remove/<int:post_id>')
def bookmarks_remove(post_id):
    bookmarks = get_bookmarks_all(current_app.config.get('BOOKMARKS_PATH'))
    delete_bookmark(current_app.config.get('BOOKMARKS_PATH'), post_id, bookmarks)

    return redirect('/', 302)
