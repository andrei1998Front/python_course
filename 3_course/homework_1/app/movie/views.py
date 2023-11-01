from flask import Blueprint, current_app, jsonify
from .dao.movie_dao import MovieDAO

movie_blueprint = Blueprint('movie_blueprint', __name__)


@movie_blueprint.route('/movie/<title>')
def movie_page(title):
    movie_dao = MovieDAO(current_app.config.get('DB_PATH'))
    return jsonify(movie_dao.get_film_by_title(title))


@movie_blueprint.route('/movie/<int:yy_from>/to/<int:yy_to>')
def movie_in_range_page(yy_from, yy_to):
    movie_dao = MovieDAO(current_app.config.get('DB_PATH'))
    return jsonify(movie_dao.get_films_in_range(yy_from, yy_to))
