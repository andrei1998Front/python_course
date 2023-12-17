from flask import request
from flask_restx import Resource, Namespace

from helpers import auth_required, admin_required
from models import Director, DirectorSchema
from setup_db import db

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        rs = db.session.query(Director).all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    def post(self):
        req_json = request.json

        nested = db.session.begin_nested()
        try:
            user = Director(**req_json)
            db.session.add(user)
        except Exception as e:
            nested.rollback()
            return "", 405

        db.session.commit()

        return "", 204


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    @auth_required
    def get(self, rid):
        r = db.session.query(Director).get(rid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, rid):
        new_director_data = request.json

        nested = db.session.begin_nested()
        try:
            director = db.session.query(Director).get(rid)

            director.name = new_director_data.name

            db.session.add(director)
        except Exception as e:
            nested.rollback()
            return "", 404

        db.session.commit()
        return "", 204

    @admin_required
    def delete(self, rid):
        nested = db.session.begin_nested()
        try:
            director = db.session.query(Director).get(rid)
            db.session.delete(director)
        except Exception as e:
            nested.rollback()
            return "", 400

        db.session.commit()
        return "", 204
