from flask import request
from flask_restful import Resource

from datab.database import User
from methods.input_sanitization import input_sanitization


def compare_password(db_password, given_password):
    return db_password == given_password


def credentials_check(username, password):
    # Get user from DB
    u = User.query.filter_by(username=username).first()

    if compare_password(u.password, password):
        # credentials check ALT TRUE
        # TODO: token generálás
        token = "token"
        return str(200) + token
    else:
        # credentials check ALT FALSE
        return str(401)


class Login(Resource):
    def post(self):
        try:
            # input sanitization
            if request.method == 'POST':
                username = input_sanitization(request.form['username'])
                password = input_sanitization(request.form['password'])
            else:
                # raise Exception("Not post", request.method)
                return str(403)

            # credentials check
            return credentials_check(username, password)

        except Exception as e:
            print(e)
