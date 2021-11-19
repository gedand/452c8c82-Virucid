import string
from datetime import date
import os
from random import random, SystemRandom

from flask import request
from flask_restful import Resource

from datab.database import CAFFFiles
from datab.shared import db
from methods.input_sanitization import input_sanitization
from methods.parsing import parsing
from methods.token_valid import token_valid


def save_file(file):
    # TODO: elmentés és path visszadás
    base_path = 'files/'
    N = 16
    name = ''.join(SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(N))
    path = base_path + name + '.txt'
    exists = True
    counter = 0
    while exists and counter < 1000:
        try:
            f = open(path, 'x')
            exists = False
        except:
            counter += 1
            pass

    f.write("dummy\n" + file)
    return path


class Upload(Resource):
    def post(self):
        try:
            # TODO: dummy
            if token_valid('dummy') and request.method == 'POST':

                file = request.form['file']
                # parsing
                parsed_file = parsing(file)

                if parsed_file is not None:
                    # parsing ALT TRUE

                    # send_path_with_date_to_database
                    path_to_file = save_file(parsed_file)
                    file = CAFFFiles(date=date.today(), location=path_to_file)
                    db.session.add(file)
                    db.session.commit()

                    # return str(path_to_file)  # --- real
                    return str(CAFFFiles.query.all())  # --- debug
                else:
                    # parsing ALT FALSE
                    return str(415)
            else:
                return str(403)
        except Exception as e:
            print(e)
