import jwt
import json

import datetime
import calendar

from flask import request
from flask_restx import Resource, Namespace

from constants import JWT_SECRET, JWT_ALGORTHM, AVAILABLE_TIME_TYPES
from exceptions import TimeTypeError
from setup_db import db

from models import User

auth_ns = Namespace('auth')


def create_period(time_type, time_count):
    if time_type not in AVAILABLE_TIME_TYPES:
        raise TimeTypeError('Incorrect time type')

    match time_type:
        case "days":
            return datetime.datetime.utcnow() + datetime.timedelta(days=time_count)
        case "seconds":
            return datetime.datetime.utcnow() + datetime.timedelta(seconds=time_count)
        case "microseconds":
            return datetime.datetime.utcnow() + datetime.timedelta(microseconds=time_count)
        case "minutes":
            return datetime.datetime.utcnow() + datetime.timedelta(minutes=time_count)
        case "hours":
            return datetime.datetime.utcnow() + datetime.timedelta(hours=time_count)
        case "weeks":
            return datetime.datetime.utcnow() + datetime.timedelta(weeks=time_count)


def generate_token(data, time_type, time_count):
    period = create_period(time_type, time_count)
    data["exp"] = calendar.timegm(period.timetuple())
    return jwt.encode(data, JWT_SECRET, JWT_ALGORTHM)


def get_tokens(data):
    access_token = generate_token(data, 'minutes', 30)
    refresh_token = generate_token(data, 'days', 130)

    return {"access_token": access_token, "refresh_token": refresh_token}


@auth_ns.route('/')
class AuthsView(Resource):
    def post(self):
        data = request.json
        user_name = data.get("username")
        password = data.get("password")

        user = db.session.query(User).filter(User.username == user_name).first()

        if user is None or user.compare_password(password) is False:
            return "no such user or wrong username and/or password", 404

        user_data = {
            "username": user.username,
            "password": user.password,
            "role": user.role
        }

        tokens = get_tokens(data)
        return tokens, 201

    def put(self):
        refresh_token = request.json.get("username")

        try:
            data = jwt.decode(jwt=refresh_token, key=JWT_SECRET, algorithms=JWT_ALGORTHM)
            username = data.get("username")
            password = data.get("password")

            user = db.session.query(User).filter(username=username).first()

            if user is None or user.password != password:
                return "no such user or wrong username and/or password", 404

            tokens = get_tokens(data)
            return tokens, 201
        except jwt.ExpiredSignatureError as ex:
            return "token expired", 401
        except jwt.InvalidTokenError as ex:
            return "token is not valid", 401
