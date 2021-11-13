import json
from flask import Flask
from flask_restful import Api, Resource
from random import randint

import numpy as np

app = Flask(__name__)
api = Api(app)


class registration(Resource):
    def post(self, username, password):
        return 0

class login(Resource):
    def post(self, username, password):
        token = 0
        return token

class download(Resource):
    def get(self, token, filename):
        return 0

class upload(Resource):
    def post(self, token, file):
        return 0

class comment(Resource):
    def post(self, token, filename, comment):
        return 0

class search(Resource):
    def get(self, token, all, filename):
        return 0

class delete(Resource):
    def post(self, token, filename):
        return 0


api.add_resource(registration, "/registration/<string:username>/<string:password>")
api.add_resource(login, "/login/<string:username>/<string:password>")
api.add_resource(download, "/download/<int:token>/<string:filename>")
api.add_resource(upload, "/upload/<int:token>/<object??:file>")
api.add_resource(comment, "/comment/<int:token>/<string:filename>/<string:comment>")
api.add_resource(search, "/search/<int:token>/<bool:all>/<string:filename>")
api.add_resource(delete, "/delete/<int:token>/<string:filename>")

if __name__ == '__main__':
    app.run(debug=True)
