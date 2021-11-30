import os
from logging.config import dictConfig

from Crypto.Random import get_random_bytes
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

from datab.database import User
from datab.shared import db
from helper.admin_helper import AdminHelper
from helper.password_helper import PasswordHelper
from resources.comment import Comment
from resources.delete import Delete
from resources.download import Download
from resources.login import Login
from resources.registration import Registration
from resources.search import Search
from resources.upload import Upload

# Configure logging first
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default',
            'level': 'DEBUG'
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'default',
            'filename': 'log/api.log',
            'mode': 'a'
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['wsgi', 'file']
    }
})

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db.init_app(app)

# File size limit
app.config['MAX_CONTENT_LENGTH'] =20 * 1024 * 1024

# JWT Token init
app.config['JWT_SECRET_KEY'] = get_random_bytes(32)
jwt = JWTManager(app)


# Set JWT custom claims
@jwt.additional_claims_loader
def add_claims_to_access_token(user):
    return {
        'username': user.username,
        'is_admin': user.is_admin
    }


# Generate JWT identity
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


db.drop_all()
db.create_all()

AdminHelper.add_admin_user()

if not os.path.exists("files"):
    os.makedirs("files")

if not os.path.exists("files/caff"):
    os.makedirs("files/caff")

if not os.path.exists("files/img"):
    os.makedirs("files/img")

api.add_resource(Registration, "/registration")
api.add_resource(Login, "/login")
api.add_resource(Download, "/download/<string:filename>")
api.add_resource(Upload, "/upload")
api.add_resource(Comment, "/comment")
api.add_resource(Search, "/search")
api.add_resource(Delete, "/delete")

if __name__ == '__main__':
    app.run(debug=True)