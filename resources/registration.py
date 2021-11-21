from flask import request
from flask_restful import Resource
from marshmallow import Schema, fields, ValidationError
from datab.database import User
from datab.shared import db
from flask import current_app  as app
from flask_api import status
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes

from validators.registration_validator import RegistrationValidator

class RegistrationSchema(Schema):
    validator = RegistrationValidator()
    username = fields.Str(required=True,error_messages={"required": "Username is required."}, validate=validator.username_check)
    password = fields.Str(required=True, error_messages={"required": "Password is required."}, validate=validator.password_check)

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
            print(password_hash)
            guest = User(username=username, password=password_hash, salt=salt, is_admin=0)
            db.session.add(guest)
            db.session.commit()
            # successful_registration_feedback
            return 'User successfully registered', status.HTTP_200_OK
        except ValidationError as v:
            app.logger.error(v)
            return str(v), status.HTTP_400_BAD_REQUEST
        except Exception as e:
            app.logger.error(e)
            return 'SERVER ERROR', status.HTTP_500_INTERNAL_SERVER_ERROR
    
    def hash_password(self, password):
        salt = get_random_bytes(16)
        return PBKDF2(password.encode('UTF-8'), salt, dkLen=16, count=200000, hmac_hash_module=SHA512), salt