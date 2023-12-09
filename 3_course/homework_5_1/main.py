from flask import Flask
from flask_restx import Api

from app.config import Config
from app.setup_db import db
from app.views.movies import movie_ns
from app.views.genres import genre_ns
from app.views.directors import director_ns


# функция создания основного объекта app
def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


def create_data(app, db):
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    app = create_app(Config())
    create_data(app, db)
    app.run(host="localhost", port=10001, debug=True)



