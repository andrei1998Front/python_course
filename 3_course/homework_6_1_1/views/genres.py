from flask import request
from flask_restx import Resource, Namespace

from helpers import auth_required, admin_required
from models import Genre, GenreSchema
from setup_db import db

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        rs = db.session.query(Genre).all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    def post(self):
        req_json = request.json

        nested = db.session.begin_nested()
        try:
            user = Genre(**req_json)
            db.session.add(user)
        except Exception as e:
            nested.rollback()
            return "", 405

        db.session.commit()

        return "", 204


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    @auth_required
    def get(self, rid):
        r = db.session.query(Genre).get(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, bid):
        genre = db.session.query(Genre).get(bid)
        req_json = request.json

        genre.name = req_json.name
        db.session.add(genre)
        db.session.commit()
        return "", 204

    @admin_required
    def delete(self, gid):
        genre = db.session.query(Genre).get(gid)

        db.session.delete(genre)
        db.session.commit()
        return "", 204
