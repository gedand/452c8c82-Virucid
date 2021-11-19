import os

from flask import request
from flask_restful import Resource

from datab.database import CAFFFiles
from datab.shared import db
from methods.token_valid import token_valid


# TODO: is_admin?
def is_admin():
    return True


class Delete(Resource):
    def post(self):
        try:
            # TODO: dummy
            if token_valid('dummy') and request.method == 'POST' and is_admin():
                # is_admin ALT TRUE
                # id_exists ALT TRUE
                fileid = request.form['fileid']
                g = CAFFFiles.query.get(fileid)
                if g:
                    os.remove(g.location)
                    db.session.delete(g)
                    db.session.commit()
                    return str(200)
                else:
                    # id_exists ALT FALSE
                    return str(404)
            else:
                # is_admin ALT FALSE
                # raise Exception("Not post", request.method)
                return str(403)
        except Exception as e:
            print(e)
