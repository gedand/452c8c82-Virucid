from flask import request
from flask_restful import Resource
from marshmallow import Schema, fields, ValidationError
from datab.database import User
from flask import current_app as app
from helper.error_message import ErrorMessage
from validators.username_validator import UsernameValidator
from validators.password_validator import PasswordValidator
from helper.password_helper import PasswordHelper

from flask_jwt_extended import create_access_token
from flask import jsonify


class LoginSchema(Schema):
    username_validator = UsernameValidator()
    password_validator = PasswordValidator()
    username = fields.Str(required=True, error_messages={"required": "Username is required."},
                          validate=username_validator.username_login)
    password = fields.Str(required=True, error_messages={"required": "Password is required."},
                          validate=password_validator.password_check)


class Login(Resource):
    def __init__(self):
        super().__init__()
        self.schema = LoginSchema()

    def post(self):
        try:
            # input sanitization
            credentials = self.schema.load(request.json)
            username = credentials['username']
            password = credentials['password']

            # credentials check
            return credentials_check(username, password)

        except (ValidationError, ValueError) as v:
            app.logger.error(v)
            return ErrorMessage.forbidden("Incorrect username or password")
        except Exception as e:
            app.logger.error(e)
            return ErrorMessage.server()


def compare_password(db_password, given_password):
    return db_password == given_password


def credentials_check(username, password):
    # Get user from DB
    user = User.query.filter_by(username=username).first()
    if user is None:
        raise ValueError('User does not exist')
    if check_password(user, password):
        app.logger.info('Generating access token')
        access_token = create_access_token(identity=user).decode('utf-8')
        return jsonify({'access_token': access_token})
    else:
        raise ValueError('Passwords do not match')


def check_password(user_in_db, password):
    salt_in_db = user_in_db.salt
    db_password_hash = user_in_db.password
    login_password_hash = PasswordHelper.hash_password(password, salt_in_db)
    return db_password_hash == login_password_hash
