from datab.shared import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(32), unique=False, nullable=False)
    salt = db.Column(db.String(32), unique=False, nullable=False)
    is_admin = db.Column(db.Integer(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def to_json(self):
        user_object = {
            'username': self.username,
            'access_token': self.access_token
        }


class CAFFFiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=False, nullable=False)
    filename = db.Column(db.String, unique=True, nullable=False)
    # img_location = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        # return " - ".join(['CAFF', str(self.id), str(self.date), str(self.location)])
        return "||".join([str(self.id), str(self.filename)])


class CAFFComments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_id = db.Column(db.Integer, unique=False, nullable=False)
    comment = db.Column(db.String(), unique=False, nullable=False)

    def __repr__(self):
        return "||".join([str(self.file_id), str(self.comment)])
