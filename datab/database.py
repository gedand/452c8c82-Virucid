from datab.shared import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    is_admin = db.Column(db.Integer(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class CAFFFiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=False, nullable=False)
    location = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        # return " - ".join(['CAFF', str(self.id), str(self.date), str(self.location)])
        return "||".join([str(self.id), str(self.location)])


class CAFFComments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(), unique=False, nullable=False)

    def __repr__(self):
        return " - ".join(['CAFF comment', str(self.id), str(self.comment)])