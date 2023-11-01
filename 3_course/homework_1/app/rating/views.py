from flask import Blueprint, current_app, jsonify
from .dao.rating_dao import RatingDao

rating_blueprint = Blueprint("rating_blueprint", __name__)


@rating_blueprint.route('/rating/<rating>')
def rating_page(rating):
    rating_dao = RatingDao(current_app.config.get('DB_PATH'))
    films_by_rating = rating_dao.get_film_by_rating(rating)

    return jsonify(films_by_rating)