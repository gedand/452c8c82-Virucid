import json
from flask import Flask
from flask_restful import Api, Resource
from random import randint

import numpy as np

app = Flask(__name__)
api = Api(app)

#TODO: token majd Sanyi nem a bodyban

class registration(Resource):
    def post(self, username, password):
        return 0

class login(Resource):
    def post(self, username, password):
        token = 0
        return token

class download(Resource):
    def get(self, filename):
        return 0

class upload(Resource):
    def post(self, file):
        return 0

class comment(Resource):
    def post(self, filename, comment):
        return 0

class search(Resource):
    def get(self, all, filename):
        return 0

class delete(Resource):
    def post(self, filename):
        return 0


api.add_resource(registration, "/registration/<string:username>/<string:password>")
api.add_resource(login, "/login/<string:username>/<string:password>")
api.add_resource(download, "/download/<string:filename>")
api.add_resource(upload, "/upload/<string:file>")
api.add_resource(comment, "/comment/<string:filename>/<string:comment>")
api.add_resource(search, "/search/<bool:all>/<string:filename>")
api.add_resource(delete, "/delete/<string:filename>")

if __name__ == '__main__':
    app.run(debug=True)
