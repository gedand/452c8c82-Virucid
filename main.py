import json
from operator import and_

from flask import Flask
from flask_restful import Api, Resource
from random import randint
import numpy as np
from datetime import date
# from database import db
# from database import User

app = Flask(__name__)
api = Api(app)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


# engine = db.create_engine('sqlite:///census.sqlite')
# connection = engine.connect()
# metadata = db.MetaData()
# census = db.Table('census', metadata, autoload=True, autoload_with=engine)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class CAFF(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    # TODO: Milyen path?
    file = db.Column(db.String)

    def __repr__(self):
        return " - ".join(['CAFF', str(self.id), str(self.date), str(self.file)])


db.drop_all()
db.create_all()


# TODO: token majd Sanyi nem a bodyban

def input_sanitation(input):
    # TODO: implement
    return input


def token_valid(token):
    # TODO: implement
    return True


def parsing(file):
    # TODO: implement
    return file


class registration(Resource):
    def post(self, username, password):
        username = input_sanitation(username)
        password = input_sanitation(password)

        if self.is_username_available(username):
            if self.password_complexity_check(password):
                guest = User(username=username, password=password)
                db.session.add(guest)
                db.session.commit()
                return str('Successful registration!')
            else:
                return str('Bad password')
        else:
            return str('Error')

    def is_username_available(self, username):
        u = User.query.filter_by(username=username).first()
        if u:
            return False
        else:
            return True

    def password_complexity_check(self, password):
        # TODO: implement
        return True


class login(Resource):
    def post(self, username, password):
        username = input_sanitation(username)
        password = input_sanitation(password)

        return self.credentials_check(username, password)

    def credentials_check(self, username, password):
        # Get user from DB
        u = User.query.filter_by(username=username).first()

        if self.compare_password(u.password, password):
            # TODO: token generálás
            return str('Succesful login + token')
        else:
            return str('Error')

    def compare_password(self, db_password, given_password):
        return db_password == given_password


class download(Resource):
    def get(self, filename):
        return 0


class upload(Resource):
    def post(self, file):
        if token_valid('dummy'):
            parsed_file = parsing(file)
            if parsed_file is not None:
                file = CAFF(date=date.today(), file=parsed_file)
                db.session.add(file)
                db.session.commit()
                return str(CAFF.query.all())
            else:
                return str('Error - parsing')
        else:
            return str('Error')


class comment(Resource):
    def post(self, filename, comment):
        return 0


class search(Resource):
    def get(self, get_all, from_date, to_date):
        if token_valid('dummy'):
            if int(get_all) == 1:
                return str(CAFF.query.all())
            else:
                u = db.session.query(CAFF).filter(
                    and_(CAFF.date <= date.fromisoformat(to_date), CAFF.date >= date.fromisoformat(from_date)))

                strr = ""
                for row in u:
                    strr += str(row) + '\n'

                return strr
        else:
            return str('Error')



class delete(Resource):
    def post(self, filename):
        return 0


api.add_resource(registration, "/registration/<string:username>/<string:password>")
api.add_resource(login, "/login/<string:username>/<string:password>")
api.add_resource(download, "/download/<string:filename>")
api.add_resource(upload, "/upload/<string:file>")
api.add_resource(comment, "/comment/<string:filename>/<string:comment>")
api.add_resource(search, "/search/<int:get_all>/<string:from_date>/<string:to_date>")
api.add_resource(delete, "/delete/<string:filename>")

if __name__ == '__main__':
    app.run(debug=True)
