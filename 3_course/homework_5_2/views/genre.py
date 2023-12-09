from implementerd import genre_service
from flask_restx import Resource, Namespace
from dao.model.genre import GenreSchema

genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        return genres_schema.dumps(genre_service.get_all())


@genre_ns.route('/<int:id>')
class GenreView(Resource):
    def get(self, id: int):
        return genre_schema.dumps(genre_service.get_one(id))
