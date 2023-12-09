# app.py

from flask import Flask, request
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

movie_ns = api.namespace('movies')
director_ns = api.namespace('directors')
genre_ns = api.namespace('genres')

class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")


class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class DirectorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


movie_schema = MovieSchema(many=True)
director_schema = DirectorSchema()
genre_schema = GenreSchema()

@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        all_movies = Movie.query

        if director_id is not None and genre_id is not None:
            return movie_schema.dumps(all_movies.filter(
                Movie.director_id == director_id, Movie.genre_id == genre_id
            )), 200
        if director_id is not None:
            return movie_schema.dumps(all_movies.filter(Movie.director_id == director_id)), 200
        elif genre_id is not None:
            return movie_schema.dumps(all_movies.filter(Movie.genre_id == genre_id)), 200

        return movie_schema.dumps(all_movies.all()), 200


@movie_ns.route('/<int:id>')
class MovieView(Resource):
    def get(self, id: int):
        movie = Movie.query.get(id)
        return movie_schema.dump(movie, many=False), 200


@director_ns.route('/', strict_slashes=False)
class DirectorsView(Resource):
    def post(self):
        req_json = request.json

        nested = db.session.begin_nested()

        try:
            new_director = Director(**req_json)
            db.session.add(new_director)
        except Exception as e:
            return "Ошибка!", 405

        db.session.commit()
        return "", 201


@director_ns.route('/<int:id>')
class DirectorView(Resource):
    def put(self, id: int):
        director = Director.query.get(id)
        req_json = request.json

        nested = db.session.begin_nested()

        try:
            director.name = req_json.get('name')
            db.session.add(director)
        except Exception as e:
            return "Ошибка!", 405

        db.session.commit()
        return "", 200

    def delete(self, id: int):
        director = Director.query.get(id)

        nested = db.session.begin_nested()

        try:
            db.session.delete(director)
        except Exception as e:
            return "Ошибка!", 404

        db.session.commit()
        return "", 200


@genre_ns.route('/', strict_slashes=False)
class GenreView(Resource):
    def post(self):
        req_json = request.json

        nested = db.session.begin_nested()

        try:
            new_genre = Genre(**req_json)
            db.session.add(new_genre)
        except Exception as e:
            return "Ошибка!", 405


        db.session.commit()
        return "", 201


@genre_ns.route('/<int:id>')
class GenreView(Resource):
    def put(self, id: int):
        genre = Genre.query.get(id)
        req_json = request.json

        nested = db.session.begin_nested()

        try:
            genre.name = req_json.get('name')
            db.session.add(genre)
        except Exception as e:
            return "Ошибка!", 404

        db.session.commit()
        return "", 200

    def delete(self, id: int):
        genre = Genre.query.get(id)

        nested = db.session.begin_nested()

        try:
            db.session.delete(genre)
        except Exception as e:
            return "Ошибка!", 404

        db.session.commit()
        return "", 200

if __name__ == '__main__':
    app.run(debug=True)
