from logging.config import dictConfig

from Crypto.Random import get_random_bytes
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

from datab.shared import db
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
# db = SQLAlchemy(app)
db.app = app
db.init_app(app)

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


# engine = db.create_engine('sqlite:///census.sqlite')
# connection = engine.connect()
# metadata = db.MetaData()
# census = db.Table('census', metadata, autoload=True, autoload_with=engine)

# TODO: Kiszedni a végén a kommentet is
#db.drop_all()
db.create_all()

api.add_resource(Registration, "/registration")
api.add_resource(Login, "/login")
api.add_resource(Download, "/download/<string:filename>")
api.add_resource(Upload, "/upload")
api.add_resource(Comment, "/comment")
api.add_resource(Search, "/search")
api.add_resource(Delete, "/delete")

if __name__ == '__main__':
    # print(os.getcwd())
    # path = os.getcwd()
    # os.chdir(os.getcwd()+"\\tmp_caff")
    # print(os.getcwd())
    # os.system("parser.exe 1.caff")
    # os.chdir(path)
    # print(os.getcwd())

    # f = os.getcwd()+"\\tmp_caff\\parser.exe tmp_caff\\1.caff"
    # print(f)
    # os.system(f)
    # print(os.system("cd tmp_caff"))
    # print(os.getcwd())
    # os.system(os.getcwd()+"\\tmp_caff\\.\\parser.exe 1.caff")
    # print(os.getcwd(), 'mi')
    # subprocess.call([os.getcwd()+"\\tmp_caff\\parser.exe", '1.caff'], cwd=os.getcwd())
    app.run(debug=True)
