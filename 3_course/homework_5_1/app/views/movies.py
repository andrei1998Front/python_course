from flask_restx import Resource, Namespace
from flask import request
from app.models import MovieSchema, Movie
from app.setup_db import db

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get("director_id")
        genre_id = request.args.get("genre_id")
        year = request.args.get("year")

        movies = Movie.query

        if director_id is not None:
            return movies_schema.dumps(movies.filter(Movie.director_id == director_id)), 200
        elif genre_id is not None:
            return movies_schema.dumps(movies.filter(Movie.genre_id == genre_id)), 200
        elif year is not None:
            return movies_schema.dumps(movies.filter(Movie.year == year)), 200

        return movies_schema.dumps(movies.all()), 200

    def post(self):
        req_json = request.json

        nested = db.session.begin_nested()

        try:
            new_movie = Movie(**req_json)
            print(new_movie)
            db.session.add(new_movie)
        except Exception as e:
            nested.rollback()
            return "Ошибка!", 405

        db.session.commit()
        return "", 201, {"location": f"/movies/{new_movie.id}"}


@movie_ns.route('/<int:id>')
class MovieView(Resource):
    def get(self, id: int):
        movie = Movie.query.get(id)
        return movie_schema.dumps(movie), 200

    def put(self, id: int):
        movie = Movie.query.get(id)
        req_json = request.json

        nested = db.session.begin_nested()

        try:
            movie.title = req_json.get("title")
            movie.description = req_json.get("description")
            movie.year = req_json.get("year")
            movie.rating = req_json.get("rating")
            movie.genre_id = req_json.get("genre_id")
            movie.director_id = req_json.get("director_id")
            db.session.add(movie)
        except Exception as e:
            nested.rollback()
            return "Ошибка!", 404,

        db.session.commit()
        return "", 204,  {"location": f"/movies/{movie.id}"}

    def delete(self, id: int):
        movie = Movie.query.get(id)

        nested = db.session.begin_nested()

        try:
            db.session.delete(movie)
        except Exception as e:
            nested.rollback()
            return "Ошибка!", 404

        db.session.commit()
        return "", 204, {"location": f"/movies/{movie.id}"}
