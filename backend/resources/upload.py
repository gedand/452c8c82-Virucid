import string
from datetime import date
from random import SystemRandom

from datab.database import CAFFFiles
from datab.shared import db
from flask import current_app as app
from flask import jsonify
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from helper.error_message import ErrorMessage
from helper.parsing import parsing
from helper.user_helper import UserHelper
from marshmallow import Schema, fields, ValidationError
from validators.upload_validator import UploadValidator
from validators.filename_validator import FileNameValidator


class UploadSchema(Schema):
    file = fields.Raw(required=True, error_messages={"required": "File is required."},
                      validate=UploadValidator().validate)


class Upload(Resource):
    def __init__(self):
        super().__init__()
        self.schema = UploadSchema()

    @jwt_required()
    def post(self):
        try:
            user_id = get_jwt_identity()
            UserHelper.get_user(id=user_id)
            file = self.schema.load(request.files)['file']

            extension = file.filename.split('.')[1]
            accepted_extensions = ['caff']
            if extension not in accepted_extensions:
                raise ValidationError("Filename has unsupported extension")

            # parsing
            caff_filename = parsing(file)
            if caff_filename is not None:
                file = CAFFFiles(date=date.today(), filename=caff_filename)
                db.session.add(file)
                db.session.commit()
                q = CAFFFiles.query.all()

                ret_files = []

                for row in q:
                    ret_files.append(row.filename)
                return jsonify({'files': ret_files})

            else:
                raise ValueError('Parsed_file is None')

        except (ValidationError, ValueError) as v:
            app.logger.error(v)
            return ErrorMessage.forbidden("Something is wrong with the file")
        except Exception as e:
            app.logger.error(e)
            return ErrorMessage.server()
