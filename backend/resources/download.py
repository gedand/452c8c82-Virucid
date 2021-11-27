from flask import send_from_directory, current_app, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import Schema, fields, ValidationError
from flask import current_app as app
from datab.database import CAFFFiles
from helper.error_message import ErrorMessage
from helper.user_helper import UserHelper
from validators.download_validator import DownloadValidator


class Download(Resource):
    @jwt_required()
    def get(self, filename):
        try:
            user_id = get_jwt_identity()
            UserHelper.get_user(id=user_id)

            DownloadValidator().validate(filename)
            g = CAFFFiles.query.filter_by(caff_location=filename).first()
            if g is None:
                raise ValueError("File couldn't be found in DB")

            # TODO: különválasztani, amikor kép, és amikor caff fájlt ad vissza
            return send_from_directory(current_app.root_path, 'files/' + g.filename, as_attachment=True)

        except (ValidationError, ValueError) as v:
            app.logger.error(v)
            return ErrorMessage.forbidden("Filename is not correct or file couldn't be found")
        except Exception as e:
            app.logger.error(e)
            return ErrorMessage.server()
