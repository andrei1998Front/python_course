from flask import Blueprint, render_template, request, current_app

from utils import get_posts_all, search_for_posts

search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates')


@search_blueprint.route('/search')
def search_page():
    search_string = request.args.get('s')
    posts = get_posts_all(current_app.config.get('POSTS_PATH'), current_app.config.get('BOOKMARKS_PATH'))
    found_posts = search_for_posts(search_string, posts)

    return render_template('search.html', posts=found_posts, search_string=search_string)



