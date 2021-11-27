from flask import request, jsonify
from flask import current_app as app
from flask_restful import Resource
from flask import request
from marshmallow import Schema, fields, ValidationError

from datab.database import CAFFComments, CAFFFiles
from datab.shared import db
from helper.json_helper import JsonHelper
from helper.parsing import parsing
from flask_jwt_extended import jwt_required, get_jwt_identity

from helper.user_helper import UserHelper
from validators.comment_validator import CommentValidator
from validators.file_id_validator import FileIdValidator
from validators.upload_validator import UploadValidator
from helper.error_message import ErrorMessage


# TODO: hol adjuk vissza a frontendnek
class CommentSchema(Schema):
    file_id = fields.Number(required=True, error_messages={
                            "required": "File id is required."},
                            validate=FileIdValidator().validate)
    comment = fields.Str(validate=CommentValidator().validate)


class Comment(Resource):
    def __init__(self):
        super().__init__()
        self.schema = CommentSchema()

    @jwt_required()
    def post(self):
        try:
            user_id = get_jwt_identity()
            UserHelper.get_user(id=user_id)

            resp = self.schema.load(request.form)
            file_id = resp['file_id']
            comment = resp['comment'] if 'comment' in resp else None

            # id_exists
            g = CAFFFiles.query.get(file_id)
            if g is None:
                raise ValueError("File ID couldn't be found in DB")

            if comment:
                comment = CAFFComments(file_id=int(file_id), comment=comment)
                db.session.add(comment)
                db.session.commit()

            q = CAFFComments.query.filter_by(file_id=file_id)

            ret_comments = []
            num = 1
            print(q)
            # TODO: kommentek is menjenek hozzá
            for row in q:
                ret_comments.append(row.comment)
            return jsonify({'comments': ret_comments})

        except (ValidationError, ValueError) as v:
            app.logger.error(v)
            return ErrorMessage.forbidden("Something is wrong with the comment or the id")
        except Exception as e:
            app.logger.error(e)
            return ErrorMessage.server()
