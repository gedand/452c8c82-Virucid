from flask import request
from flask_restful import Resource

from datab.database import User
from datab.shared import db
from methods.input_sanitization import input_sanitization


class Registration(Resource):
    def post(self):
        try:
            # input sanitization
            if request.method == 'POST':
                username = input_sanitization(request.form['username'])
                password = input_sanitization(request.form['password'])
            else:
                # raise Exception("Not post", request.method)
                return str(403)
            # is_username_available
            if self.is_username_available(username):
                # is_username_available: ALT TRUE

                # password_complexity_check
                if self.password_complexity_check(password):
                    # password_complexity_check ALT TRUE

                    # send_registration_parameters
                    guest = User(username=username, password=password, is_admin=0)
                    db.session.add(guest)
                    db.session.commit()
                    # successful_registration_feedback
                    return str(200)
                else:
                    # password_complexity_check ALT FALSE
                    return str(401)
            else:
                # is_username_available: ALT FALSE
                return str(403)
        except Exception as e:
            print(e)

    def is_username_available(self, username):
        u = User.query.filter_by(username=username).first()
        if u:
            return False
        else:
            return True

    def password_complexity_check(self, password):
        # TODO: implement
        return True
