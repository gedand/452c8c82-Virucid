from operator import and_

from datab.database import CAFFFiles
from datab.shared import db
from flask import current_app as app
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from helper.date_converter import DateConverter
from helper.error_message import ErrorMessage
from helper.user_helper import UserHelper
from marshmallow import Schema, ValidationError, fields


class SearchSchema(Schema):
    start_date = fields.Date('%Y-%m-%d')
    end_date = fields.Date('%Y-%m-%d')


class Search(Resource):
    def __init__(self):
        super().__init__()
        self.schema = SearchSchema()

    @jwt_required()
    def get(self):
        try:
            user_id = get_jwt_identity()
            UserHelper.get_user(id=user_id)
            dates = self.schema.load(request.args)
            from_date, to_date = DateConverter.convert(dates)
            if (not from_date) and (not to_date):
                q = CAFFFiles.query.all()
            else:
                q = db.session.query(CAFFFiles).filter(
                    and_(CAFFFiles.date <= to_date,
                         CAFFFiles.date >= from_date))

            ret_files = []

            for row in q:
                ret_files.append(row.filename)
            return jsonify({'files': ret_files})


        except (ValidationError, ValueError) as v:
            app.logger.error(v)
            return ErrorMessage.bad_request("Something is wrong with the dates")
        except Exception as e:
            app.logger.error(e)
            return ErrorMessage.server()
