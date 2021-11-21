from datetime import date
from operator import and_

from flask_restful import Resource

from datab.database import CAFFFiles
from datab.shared import db


class Search(Resource):
    def get(self, get_all, from_date, to_date):
        try:
            # TODO: dummy
            if token_valid('dummy'):

                if int(get_all) == 1:
                    # Nincs definiálva a szekvencia diagramon TODO: maybe hozzáadás
                    return str(CAFFFiles.query.all())
                else:
                    # search(from_date,to_date)

                    u = db.session.query(CAFFFiles).filter(
                        and_(CAFFFiles.date <= date.fromisoformat(to_date),
                             CAFFFiles.date >= date.fromisoformat(from_date)))
                    return_str = ""
                    num = 0
                    for row in u:
                        # formátum: (ID||path;)*
                        return_str += str(row) + ';'
                        num += 1

                    if num != 0:
                        # search(from_date,to_date) ALT TRUE
                        return return_str
                    else:
                        # search(from_date,to_date) ALT FALSE
                        return str(404)
            else:
                return str(403)
        except Exception as e:
            print(e)
