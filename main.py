from flask import Flask
from flask_restful import Api

from datab.shared import db
from resources.comment import Comment
from resources.delete import Delete
from resources.download import Download
from resources.login import Login
from resources.registration import Registration
from resources.search import Search
from resources.upload import Upload

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)
db.app = app
db.init_app(app)

# engine = db.create_engine('sqlite:///census.sqlite')
# connection = engine.connect()
# metadata = db.MetaData()
# census = db.Table('census', metadata, autoload=True, autoload_with=engine)

db.drop_all()
db.create_all()

# TODO: token majd Sanyi nem a bodyban

api.add_resource(Registration, "/registration")
api.add_resource(Login, "/login")
api.add_resource(Download, "/download/<string:fileid>")
api.add_resource(Upload, "/upload")
api.add_resource(Comment, "/comment")
api.add_resource(Search, "/search/<int:get_all>/<string:from_date>/<string:to_date>")
api.add_resource(Delete, "/delete")

if __name__ == '__main__':
    app.run(debug=True)
