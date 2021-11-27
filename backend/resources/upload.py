import os
import string
import sys
from datetime import date
from random import SystemRandom

from flask import current_app as app
from flask import jsonify
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from marshmallow import Schema, fields, ValidationError

from datab.database import CAFFFiles
from datab.shared import db
from helper.error_message import ErrorMessage
from helper.json_helper import JsonHelper
from helper.parsing import parsing
from helper.user_helper import UserHelper
from validators.upload_validator import UploadValidator


def save_file(file):
    # TODO: elmentés és path visszadás
    base_path = 'files/'
    N = 16
    exists = True
    counter = 0
    while exists and counter < 1000:
        try:
            name = ''.join(SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(N))
            path = base_path + name + '.txt'
            f = open(path, 'x')
            exists = False
        except:
            counter += 1
            pass

    f.write(str(file))  # TODO: képként mentse a fájlt
    return path


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
            # parsing
            caff_filename = parsing(file)  # TODO: Robival egyeztetni
            if caff_filename is not None:
                # send_path_with_date_to_database
                # path_to_file = save_file(parsed_file).split('/')[-1]
                # TODO: itt az img_location tényleg az img_locationra kéne vonatkozzon
                file = CAFFFiles(date=date.today(), filename=caff_filename)
                db.session.add(file)
                db.session.commit()

                # return str(path_to_file)  # TODO: --- real
                files = JsonHelper.search_to_json(
                    CAFFFiles.query.all())  # TODO: most mindent listáz, bár nem feltétlen baj
                return jsonify({"content": files})
            else:
                raise ValueError('Parsed_file is None')

        except (ValidationError, ValueError) as v:
            app.logger.error(v)
            return ErrorMessage.forbidden("Something is wrong with the file")
        except Exception as e:
            app.logger.error(e)
            return ErrorMessage.server()
