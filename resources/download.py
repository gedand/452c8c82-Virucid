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
    def get(self, location):
        try:
            user_id = get_jwt_identity()
            UserHelper.get_user(id = user_id)

            g = CAFFFiles.query.filter_by(location = location).first()
            # id_exists ALT TRUE
            return send_from_directory(current_app.root_path, 'files/' + g.location, as_attachment=True)

        except (ValidationError, ValueError) as v:
            app.logger.error(v)
            return ErrorMessage.forbidden("Filename is not correct")
        except Exception as e:
            app.logger.error(e)
            return ErrorMessage.server()
