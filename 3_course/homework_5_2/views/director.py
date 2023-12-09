from implementerd import director_service
from flask_restx import Resource, Namespace
from dao.model.director import DirectorSchema

director_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        return directors_schema.dumps(director_service.get_all()), 200


@director_ns.route('/<int:id>')
class DirectorView(Resource):
    def get(self, id: int):
        return directors_schema.dumps(director_service.get_one(id)), 200
