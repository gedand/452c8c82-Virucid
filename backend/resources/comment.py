from datab.database import CAFFComments, CAFFFiles
from datab.shared import db
from flask import current_app as app
from flask import jsonify
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from helper.error_message import ErrorMessage
from helper.user_helper import UserHelper
from marshmallow import Schema, fields, ValidationError
from validators.comment_validator import CommentValidator
from validators.filename_validator import FileNameValidator


# TODO: hol adjuk vissza a frontendnek
class CommentSchema(Schema):
    filename = fields.Str(required=True, error_messages={
        "required": "Filename is required."},
                          validate=FileNameValidator().validate)
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
            filename = resp['filename']
            comment = resp['comment'] if 'comment' in resp else None

            # lekérdezzük másik queryből a fájlnevet TODO
            filename_split = filename.split('.')
            # id_exists
            file_in_db = CAFFFiles.query.filter_by(filename=filename_split[0]).first()
            if file_in_db is None:
                raise ValueError("File ID couldn't be found in DB")

            file_id = file_in_db.id

            if comment:
                comment = CAFFComments(file_id=file_id, comment=comment)
                db.session.add(comment)
                db.session.commit()

            q = CAFFComments.query.filter_by(file_id=file_id)

            ret_comments = []
            num = 1
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
