import os
from flask import request
from flask import current_app as app
from flask_jwt_extended.utils import get_jwt
from flask_restful import Resource
from flask import request
from marshmallow import Schema, fields, ValidationError

from datab.database import CAFFFiles
from datab.shared import db
from flask_jwt_extended import jwt_required, get_jwt_identity

from helper.user_helper import UserHelper
from validators.filename_validator import FileNameValidator
from helper.error_message import ErrorMessage


def is_admin(is_admin):
    if not is_admin:
        raise ValidationError('Logged in user is not admin')


class DeleteSchema(Schema):
    filename = fields.Str(required=True, error_messages={"required": "Filename is required."},
                            validate=FileNameValidator().validate)


# TODO: fájlokkal együtt hozzátartozó kommentek törlése is
# TODO: nem csak a CAFF, hanem IMG fájl törlése is
class Delete(Resource):
    def __init__(self):
        super().__init__()
        self.schema = DeleteSchema()

    @jwt_required()
    def post(self):
        try:
            user_id = get_jwt_identity()
            is_admin(get_jwt()['is_admin'])
            UserHelper.get_user(id=user_id)
            filename = self.schema.load(request.form)['filename']

            file_in_db = CAFFFiles.query.filter_by(filename=filename).first()

            if file_in_db is None:
                raise ValueError("File ID couldn't be found in DB")

            os.remove("files/" + file_in_db.filename)
            db.session.delete(file_in_db)
            db.session.commit()
            return ErrorMessage.OK()



        except (ValidationError, ValueError) as v:
            app.logger.error(v)
            return ErrorMessage.forbidden("Something is wrong with the file or user is not admin")
        except Exception as e:
            app.logger.error(e)
            return ErrorMessage.server()
