from flask import request
from flask_restful import Resource

from datab.database import CAFFFiles, CAFFComments
from datab.shared import db


# TODO: hol adjuk vissza a frontendnek

class Comment(Resource):
    def post(self):
        try:
            # TODO: dummy
            if token_valid('dummy'):
                file_id = request.form['file_id']
                comment = request.form['comment']
                # id_exists
                g = CAFFFiles.query.get(file_id)
                if g:
                    # id_exists ALT TRUE
                    comment = CAFFComments(file_id=int(file_id), comment=comment)
                    db.session.add(comment)
                    db.session.commit()
                    return str(200)
                else:
                    # id_exists ALT FALSE
                    return str(404)
            else:
                # raise Exception("Not post", request.method)
                return str(403)
        except Exception as e:
            print(e)
