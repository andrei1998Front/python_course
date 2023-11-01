from flask import Blueprint, current_app, jsonify
from .dao.genre_dao import GenreDAO
genre_blueprint = Blueprint('genre_blueprint', __name__)


@genre_blueprint.route('/genre/<genre>')
def genre_page(genre):
    genre_dao = GenreDAO(current_app.config.get('DB_PATH'))
    films_by_genre = genre_dao.get_films_by_genre(genre)

    return jsonify(films_by_genre)
