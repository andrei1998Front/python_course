from flask import request
from flask_restx import Resource, Namespace

from models import User, UserSchema
from setup_db import db

user_ns = Namespace("users")

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route("/")
class UsersViews(Resource):
    def get(self):
        return users_schema.dumps(db.session.query(User).all()), 200

    def post(self):
        nested = db.session.begin_nested()
        try:
            req_json = request.json
            user = User(**req_json)
            db.session.add(user)
        except Exception as e:
            nested.rollback()
            return "Ошибка!", 405

        db.session.commit()
        return "", 204


@user_ns.route('/<int:id>')
class UserView(Resource):
    def get(self, id):
        return users_schema.dump(db.session.query(User).get(id))

    def put(self, id):
        user = db.session.query(User).get(id)
        new_user_data = request.json

        nested = db.session.begin_nested()
        try:
            user.username = new_user_data.username
            user.password = new_user_data.password
            user.password = user.get_hash()
            user.role = new_user_data.role

            db.session.add(user)
        except Exception as e:
            nested.rollback()
            return "Ошибка!", 404

        db.session.commit()
        return "", 204

    def delete(self, id):
        user = db.session.query(User).get(id)
        try:
            db.session.delete(user)
        except Exception as e:
            return "Ошибка!", 400

        db.session.commit()

        return "", 204
