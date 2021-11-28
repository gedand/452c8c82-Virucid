from datab.database import CAFFFiles
from flask import current_app as app
from flask import send_from_directory, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from helper.error_message import ErrorMessage
from helper.user_helper import UserHelper
from marshmallow import ValidationError
from validators.download_validator import DownloadValidator


class Download(Resource):

    # accessible globally
    def get(self, filename):
        try:
            DownloadValidator().validate(filename)
            filename_split = filename.split('.')

            g = CAFFFiles.query.filter_by(filename=filename_split[0]).first()
            if g is None:
                raise ValueError("File couldn't be found in DB")

            if filename_split[1] == 'caff':
                return send_from_directory(current_app.root_path,
                                       'files/' + 'caff' + '/' + g.filename + '.' + filename_split[1],
                                       as_attachment=True)
            else:
                return send_from_directory(current_app.root_path,
                                       'files/' + 'img' + '/' + g.filename + '.' + filename_split[1],
                                       as_attachment=False)
                

            

        except (ValidationError, ValueError) as v:
            app.logger.error(v)
            return ErrorMessage.forbidden("Filename is not correct or file couldn't be found")
        except Exception as e:
            app.logger.error(e)
            return ErrorMessage.server()
