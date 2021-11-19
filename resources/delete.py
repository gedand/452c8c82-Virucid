from operator import and_
from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from methods.input_sanitization import input_sanitization
from methods.token_valid import token_valid
from methods.parsing import parsing

from datab.database import User
from datab.shared import db

class Delete(Resource):
    def post(self):
        try:
            if request.method == 'POST':
                filename = input_sanitization(request.form['filename'])
            else:
                # raise Exception("Not post", request.method)
                return str(403)
            return 0
        except Exception as e:
            print(e)