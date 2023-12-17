import jwt
from flask import request
from flask_restx import abort

from constants import JWT_SECRET, JWT_ALGORTHM


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        token = request.headers['Authorization'].split("Bearer ")[-1]

        try:
            print(token)
            jwt.decode(jwt=token, key=JWT_SECRET, algorithms=JWT_ALGORTHM)
        except Exception as e:
            print("JWT Decide Exception", e)
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        token = request.headers['Authorization'].split("Bearer ")[-1]

        try:
            data = jwt.decode(jwt=token, key=JWT_SECRET, algorithms=JWT_ALGORTHM)
            print(data)
            role = data.get("role")

            if role != 'admin':
                abort(400)
        except Exception as e:
            print("JWT Decide Exception", e)
            abort(401)
        return func(*args, **kwargs)

    return wrapper
