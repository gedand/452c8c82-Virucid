from flask import send_from_directory, current_app
from flask_restful import Resource

from datab.database import CAFFFiles
from methods.token_valid import token_valid


class Download(Resource):
    def get(self, fileid):
        try:
            # TODO: dummy
            if token_valid('dummy'):
                # CAFF_download(id)
                g = CAFFFiles.query.get(fileid)
                try:
                    # id_exists ALT TRUE
                    return send_from_directory(current_app.root_path, g.location, as_attachment=True)
                except:
                    # id_exists ALT FALSE
                    return str(404)
            else:
                return str(403)
        except Exception as e:
            print(e)
