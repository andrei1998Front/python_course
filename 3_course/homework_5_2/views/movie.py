from implementerd import movie_service
from flask import request
from flask_restx import Resource, Namespace
from dao.model.movie import MovieSchema

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        filters = {
            "director_id": request.args.get("director_id"),
            "genre_id": request.args.get("genre_id"),
            "year": request.args.get("year")
        }

        return movies_schema.dumps(movie_service.get_all(filters)), 200

    def post(self):
        req = request.json
        movie = movie_service.post(req)
        return "", 201, {"location": f"/movies/{movie.id}"}


@movie_ns.route('/<int:id>')
class MovieView(Resource):
    def get(self, id: int):
        return movie_schema.dumps(movie_service.get_one(id)), 200

    def put(self, id: int):
        req = request.json

        if "id" not in req:
            req["id"] = id

        movie_service.put(req)
        return "", 204

    def delete(self, id: int):
        movie_service.delete(id)
        return "", 204
