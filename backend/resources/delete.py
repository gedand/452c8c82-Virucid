import os

from datab.database import CAFFFiles, CAFFComments
from datab.shared import db
from flask import current_app as app
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from flask_restful import Resource
from helper.error_message import ErrorMessage
from helper.user_helper import UserHelper
from marshmallow import Schema, fields, ValidationError
from validators.filename_validator import FileNameValidator


def is_admin(is_admin):
    if not is_admin:
        raise ValidationError('Logged in user is not admin')


class DeleteSchema(Schema):
    filename = fields.Str(required=True, error_messages={"required": "Filename is required."},
                          validate=FileNameValidator().validate)


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
            filename_split = filename.split('.')
            file_in_db = CAFFFiles.query.filter_by(filename=filename_split[0]).first()

            if file_in_db is None:
                raise ValueError("File ID couldn't be found in DB")

            os.remove("files/caff/" + file_in_db.filename + ".caff")
            os.remove("files/img/" + file_in_db.filename + ".jpg")
            db.session.delete(file_in_db)
            db.session.commit()
            delete_comments(file_in_db.id)
            return ErrorMessage.OK()

        except (ValidationError, ValueError) as v:
            app.logger.error(v)
            return ErrorMessage.forbidden("Something is wrong with the file or user is not admin")
        except Exception as e:
            app.logger.error(e)
            return ErrorMessage.server()


def delete_comments(file_id):
    q = CAFFComments.query.filter_by(file_id=file_id)
    for row in q:
        db.session.delete(row)
