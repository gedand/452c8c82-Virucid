from flask import request
from flask_restful import Resource

from datab.database import CAFFFiles, CAFFComments
from datab.shared import db
from methods.token_valid import token_valid


# TODO: hol adjuk vissza a frontendnek

class Comment(Resource):
    def post(self):
        try:
            # TODO: dummy
            if token_valid('dummy') and request.method == 'POST':
                fileid = request.form['fileid']
                comment = request.form['comment']
                # id_exists
                g = CAFFFiles.query.get(fileid)
                if g:
                    # id_exists ALT TRUE
                    comment = CAFFComments(fileid=int(fileid), comment=comment)
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
