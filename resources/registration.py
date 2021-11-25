from logging import error
from flask import request
from flask.json import jsonify
from flask_restful import Resource
from marshmallow import Schema, fields, ValidationError
from datab.database import User
from datab.shared import db
from flask import current_app as app
from flask_api import status
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes

from validators.username_validator import UsernameValidator
from validators.password_validator import PasswordValidator
from helper.password_helper import PasswordHelper
from helper.error_message import ErrorMessage


class RegistrationSchema(Schema):
    username_validator = UsernameValidator()
    password_validator = PasswordValidator()
    username = fields.Str(required=True, error_messages={"required": "Username is required."},
                          validate=username_validator.username_register)
    password = fields.Str(required=True, error_messages={"required": "Password is required."},
                          validate=password_validator.password_check)


class Registration(Resource):
    def __init__(self):
        super().__init__()
        self.schema = RegistrationSchema()

    def post(self):
        try:
            # Validates input
            credentials = self.schema.load(request.form)
            username = credentials['username']
            password_hash, salt = self.hash_password(credentials['password'])
            guest = User(username=username, password=password_hash, salt=salt, is_admin=0)
            db.session.add(guest)
            db.session.commit()
            # successful_registration_feedback
            app.logger.info('User ' + username + ' successfully registered')
            return ErrorMessage.OK('User ' + username + ' successfully registered')

        except ValidationError as v:
            if 'required' in str(v):
                err_message = "Username and password are required"
            elif 'taken' in str(v):
                err_message = "Username is taken"
            else:
                err_message = "Username or password does not meet requirements"
            app.logger.error(v)
            return ErrorMessage.forbidden(err_message)
        except Exception as e:
            app.logger.error(e)
            return ErrorMessage.server()

    def hash_password(self, password):
        salt = get_random_bytes(16)
        return PasswordHelper.hash_password(password, salt), salt
